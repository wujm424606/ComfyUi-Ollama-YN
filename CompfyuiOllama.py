import random

from ollama import Client
from PIL import Image
import numpy as np
import base64
from io import BytesIO
import json
import re

prompt_template = {
  "description": "",
  "long_prompt": "",
  "camera_angle_word": "",
  "style_words": "",
  "subject_words": "",
  "light_words": "",
  "environment_words": ""
}
class OllamaVision:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE",),
                "query": ("STRING", {
                    "multiline": True,
                    "default": "describe the image"
                }),
                "debug": (["enable", "disable"],),
                "url": ("STRING", {
                    "multiline": False,
                    "default": "http://127.0.0.1:11434"
                }),
                "model": ("STRING", {
                    "multiline": False,
                    "default": "llava"
                }),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "keep_alive": (["0", "60m"],),
                
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("description",)
    FUNCTION = "ollama_vision"
    CATEGORY = "Ollama"

    def ollama_vision(self, images, query,seed, debug, url, keep_alive, model):
        images_b64 = []

        for (batch_number, image) in enumerate(images):
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_bytes = base64.b64encode(buffered.getvalue())
            images_b64.append(str(img_bytes, 'utf-8'))

        client = Client(host=url)
        options = {
            "seed": seed,
        }

        if debug == "enable":
            print(f"""[Ollama Vision] 
request query params:

- query: {query}
- url: {url}
- model: {model}
- options: {options}
- keep_alive: {keep_alive}

""")

        response = client.generate(model=model, prompt=query, keep_alive=keep_alive, options=options, images=images_b64)



        return (response['response'],)


class OllamaGenerate:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "What is Art?"
                }),
                "debug": (["enable", "disable"],),
                "url": ("STRING", {
                    "multiline": False,
                    "default": "http://127.0.0.1:11434"
                }),
                "model": ("STRING", {
                    "multiline": False,
                    "default": "llama3"
                }),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "keep_alive": (["0", "60m"],),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("response",)
    FUNCTION = "ollama_generate"
    CATEGORY = "Ollama"

    def ollama_generate(self, prompt, debug, url, model, seed, keep_alive):

        client = Client(host=url)

        options = {
            "seed": seed,
        }

        if debug == "enable":
            print(f"""[Ollama Generate] 
request query params:
               
- prompt: {prompt}
- url: {url}
- model: {model}

            """)

        response = client.generate(model=model, prompt=prompt, options=options, keep_alive=keep_alive)

        if debug == "enable":
                print(f"""\n[Ollama Generate]
response:

- model: {response["model"]}
- created_at: {response["created_at"]}
- done: {response["done"]}
- eval_duration: {response["eval_duration"]}
- load_duration: {response["load_duration"]}
- eval_count: {response["eval_count"]}
- eval_duration: {response["eval_duration"]}
- prompt_eval_duration: {response["prompt_eval_duration"]}

- response: {response["response"]}

- context: {response["context"]}

- options : {options}
- keep_alive: {keep_alive}


""")

        return (response['response'],)

# https://github.com/ollama/ollama/blob/main/docs/api.md#generate-a-completion

class OllamaGenerateAdvance:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        seed = random.randint(1, 2 ** 31)
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "1个女孩在森林里散步"
                }),
                "debug": (["enable", "disable"],),
                "url": ("STRING", {
                    "multiline": False,
                    "default": "http://127.0.0.1:11434"
                }),
                # "model": ("STRING", {
                #     "multiline": False,
                #     "default": (["llama3:8b-instruct-q4_K_M", "llama3", "phi3:instruct", "phi3"],)
                # }),
                "model": (["llama3:8b-instruct-q4_K_M", "llama3", "phi3:3.8b-mini-instruct-4k-q4_K_M", "phi3", "phi3:3.8b-mini-instruct-4k-fp16"],),
                "extra_model": ("STRING", {
                    "multiline": False,
                    "default": "none"
                }),               
                "system": ("STRING", {
                    "multiline": True,
                    "default": "You are creating a prompt for Stable Diffusion to generate an image. First step: understand the input and generate a text prompt for the input. Second step: only respond in English with the prompt itself in phrase, but embellish it as needed but keep it under 200 tokens.",
                    "title":"system"
                }),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "top_k": ("FLOAT", {"default": 40, "min": 0, "max": 100, "step": 1}),
                "top_p": ("FLOAT", {"default": 0.9, "min": 0, "max": 1, "step": 0.05}),
                "temperature": ("FLOAT", {"default": 0.5, "min": 0, "max": 1, "step": 0.05}),
                "num_predict": ("FLOAT", {"default": -1, "min": -2, "max": 2048, "step": 1}),
                "tfs_z": ("FLOAT", {"default": 1, "min": 1, "max": 1000, "step": 0.05}),
                "keep_alive": (["0", "60m"],),
            },"optional": {
                "context": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("response","context",)
    FUNCTION = "ollama_generate_advance"
    CATEGORY = "Ollama"

    def ollama_generate_advance(self, prompt, debug, url, model, extra_model, system, seed, top_k, top_p,temperature,num_predict,tfs_z, keep_alive, context=None):

        client = Client(host=url)

        # num_keep: int
        # seed: int
        # num_predict: int
        # top_k: int
        # top_p: float
        # tfs_z: float
        # typical_p: float
        # repeat_last_n: int
        # temperature: float
        # repeat_penalty: float
        # presence_penalty: float
        # frequency_penalty: float
        # mirostat: int
        # mirostat_tau: float
        # mirostat_eta: float
        # penalize_newline: bool
        # stop: Sequence[str]

        options = {
            "seed": seed,
            "top_k":top_k,
            "top_p":top_p,
            "temperature":temperature,
            "num_predict":num_predict,
            "tfs_z":tfs_z,
        }

        if debug == "enable":
            print(f"""[Ollama Generate Advance]
request query params:

- prompt: {prompt}
- url: {url}
- model: {model}
- extra_model: {extra_model}
- keep_alive: {keep_alive}
- options: {options}
""")
            
        if extra_model != "none":
            model = extra_model
        response = client.generate(model=model, system=system, prompt=prompt, keep_alive=keep_alive, context=context, options=options)

        if debug == "enable":
            print(f"""\n[Ollama Generate Advance]
response:

- model: {response["model"]}
- created_at: {response["created_at"]}
- done: {response["done"]}
- eval_duration: {response["eval_duration"]}
- load_duration: {response["load_duration"]}
- eval_count: {response["eval_count"]}
- eval_duration: {response["eval_duration"]}
- prompt_eval_duration: {response["prompt_eval_duration"]}

- response: {response["response"]}

- context: {response["context"]}

""")
        return (response['response'],response['context'],)

class OllamaSpecialGenerateAdvance:
    def __init__(self):
        pass
#The default system prompt referenced https://github.com/MinusZoneAI/ComfyUI-Prompt-MZ project
    @classmethod
    def INPUT_TYPES(s):
        seed = random.randint(1, 2 ** 31)
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": f"一个小女孩在森林里"
                }),
                "debug": (["enable", "disable"],),
                "style_categories": (["none", "high quality", "photography", "illustration"],),
                "url": ("STRING", {
                    "multiline": False,
                    "default": "http://127.0.0.1:11434"
                }),
                # "model": ("STRING", {
                #     "multiline": False,
                #     "default": (["llama3:8b-instruct-q4_K_M", "llama3", "phi3:instruct", "phi3"],)
                # }),
                "model": (["llama3:8b-instruct-q4_K_M", "llama3", "phi3:3.8b-mini-instruct-4k-q4_K_M", "phi3", "phi3:3.8b-mini-instruct-4k-fp16"],),
                "extra_model": ("STRING", {
                    "multiline": False,
                    "default": "none"
                }), 
                "system": ("STRING", {
                    "multiline": True,
                    "default": """Stable Diffusion is an AI art generation model similar to DALLE-2.
Below is a list of prompts that can be used to generate images with Stable Diffusion:
- portait of a homer simpson archer shooting arrow at forest monster, front game card, drark, marvel comics, dark, intricate, highly detailed, smooth, artstation, digital illustration by ruan jia and mandy jurgens and artgerm and wayne barlowe and greg rutkowski and zdislav beksinski
- pirate, concept art, deep focus, fantasy, intricate, highly detailed, digital painting, artstation, matte, sharp focus, illustration, art by magali villeneuve, chippy, ryan yee, rk post, clint cearley, daniel ljunggren, zoltan boros, gabor szikszai, howard lyon, steve argyle, winona nelson
- ghost inside a hunted room, art by lois van baarle and loish and ross tran and rossdraws and sam yang and samdoesarts and artgerm, digital art, highly detailed, intricate, sharp focus, Trending on Artstation HQ, deviantart, unreal engine 5, 4K UHD image
- red dead redemption 2, cinematic view, epic sky, detailed, concept art, low angle, high detail, warm lighting, volumetric, godrays, vivid, beautiful, trending on artstation, by jordan grimmer, huge scene, grass, art greg rutkowski
- a fantasy style portrait painting of rachel lane / alison brie hybrid in the style of francois boucher oil painting unreal 5 daz. rpg portrait, extremely detailed artgerm greg rutkowski alphonse mucha greg hildebrandt tim hildebrandt
- athena, greek goddess, claudia black, art by artgerm and greg rutkowski and magali villeneuve, bronze greek armor, owl crown, d & d, fantasy, intricate, portrait, highly detailed, headshot, digital painting, trending on artstation, concept art, sharp focus, illustration
- closeup portrait shot of a large strong female biomechanic woman in a scenic scifi environment, intricate, elegant, highly detailed, centered, digital painting, artstation, concept art, smooth, sharp focus, warframe, illustration, thomas kinkade, tomasz alen kopera, peter mohrbacher, donato giancola, leyendecker, boris vallejo
- ultra realistic illustration of steve urkle as the hulk, intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse mucha
I want you to write me a list of detailed prompts exactly about the idea written after IDEA. Follow the structure of the example prompts. This means a very short description of the scene, followed by modifiers divided by commas to alter the mood, style, lighting, and more.
Please generate the long prompt version of the short one according to the given examples. Long prompt version should consist of 3 to 5 sentences. Long prompt version must sepcify the color, shape, texture or spatial relation of the included objects. DO NOT generate sentences that describe any atmosphere!!!""",
                    "title":"system"
                }),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "top_k": ("FLOAT", {"default": 40, "min": 0, "max": 100, "step": 1}),
                "top_p": ("FLOAT", {"default": 0.9, "min": 0, "max": 1, "step": 0.05}),
                "temperature": ("FLOAT", {"default": 0.5, "min": 0, "max": 1, "step": 0.05}),
                "num_predict": ("FLOAT", {"default": -1, "min": -2, "max": 2048, "step": 1}),
                "tfs_z": ("FLOAT", {"default": 1, "min": 1, "max": 1000, "step": 0.05}),
                "keep_alive": (["0", "60m"],),
            },"optional": {
                "context": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("response","context",)
    FUNCTION = "ollama_generate_advance"
    CATEGORY = "Ollama"

    def ollama_generate_advance(self, prompt, debug, style_categories, url, model, extra_model, system, seed,top_k, top_p,temperature,num_predict,tfs_z, keep_alive, context=None):

        prompt = f"{prompt} \nUse the following template: {json.dumps(prompt_template)}."
        client = Client(host=url)

        # num_keep: int
        # seed: int
        # num_predict: int
        # top_k: int
        # top_p: float
        # tfs_z: float
        # typical_p: float
        # repeat_last_n: int
        # temperature: float
        # repeat_penalty: float
        # presence_penalty: float
        # frequency_penalty: float
        # mirostat: int
        # mirostat_tau: float
        # mirostat_eta: float
        # penalize_newline: bool
        # stop: Sequence[str]

        options = {
            "seed": seed,
            "top_k":top_k,
            "top_p":top_p,
            "temperature":temperature,
            "num_predict":num_predict,
            "tfs_z":tfs_z,
        }

        if debug == "enable":
            print(f"""[Ollama Special Generate Advance]
request query params:

- prompt: {prompt}
- url: {url}
- model: {model}
- extra_model: {extra_model}
- keep_alive: {keep_alive}
- options: {options}
""")
        if extra_model != "none":
            model = extra_model
        response = client.generate(model=model, system=system, prompt=prompt, context=context, keep_alive=keep_alive, options=options)

        if debug == "enable":
            print(f"""\n[Ollama Generate Advance]
response:

- model: {response["model"]}
- created_at: {response["created_at"]}
- done: {response["done"]}
- eval_duration: {response["eval_duration"]}
- load_duration: {response["load_duration"]}
- eval_count: {response["eval_count"]}
- eval_duration: {response["eval_duration"]}
- prompt_eval_duration: {response["prompt_eval_duration"]}

- response: {response["response"]}

- context: {response["context"]}

""")


        #The regular expression code referenced https://github.com/MinusZoneAI/ComfyUI-Prompt-MZ project

        corresponding_prompt = dict()
        description = re.findall(
            r"\s*\**\s*\"*[Dd][Ee][Ss][Cc][Rr][Ii][Pp][Tt][Ii][Oo][Nn]\"*\s*\**\s*:\s*\**\s*\"*\s*\"*([^*\n\"]+)",
            response["response"])
        if len(description) == 0:
            description = ""
        else:
            description = description[0]


        long_prompt = re.findall(
            r"\s*\**\s*\"*[Ll][Oo][Nn][Gg][ _][Pp][Rr][Oo][Mm][Pp][Tt]\"*\s*\**\s*:\s*\**\s*\"*\s*\"*([^*\n\"]+)",
            response["response"])
        if len(long_prompt) == 0:
            long_prompt = ""
        else:
            long_prompt = long_prompt[0]
        # main_color_word = re.findall(
        #     r"\s*\**\s*\"*[Mm][Aa][Ii][Nn][ _][Cc][Oo][Ll][Oo][Rr][ _][Ww][Oo][Rr][Dd]\"*\s*\**\s*:\s*\**\s*\"*\s*\"*([^*\n\"]+)",
        #     response["response"])
        camera_angle_word = re.findall(
            r"\s*\**\s*\"*[Cc][Aa][Mm][Ee][Rr][Aa][ _][Aa][Nn][Gg][Ll][Ee][ _][Ww][Oo][Rr][Dd]\"*\s*\**\s*:\s*\**\s*\"*\s*\"*([^*\n\"]+)",
            response["response"])
        if len(camera_angle_word) == 0:
            camera_angle_word = ""
        else:
            camera_angle_word =  camera_angle_word[0]


        style_words = re.findall(
            r"\s*\**\s*\"*[Ss][Tt][Yy][Ll][Ee][ _][Ww][Oo][Rr][Dd][Ss]\"*\s*\**\s*:\s*\**\s*\"*\s*\"*([^*\n\"]+)",
            response["response"])
        if len(style_words) == 0:
            style_words = ""
        else:
            style_words =  style_words[0]


        subject_words = re.findall(
            r"\s*\**\s*\"*[Ss][Uu][Bb][Jj][Ee][Cc][Tt][ _][Ww][Oo][Rr][Dd][Ss]\"*\s*\**\s*:\s*\**\s*\"*\s*\"*([^*\n\"]+)",
            response["response"])
        if len(subject_words) == 0:
            subject_words = ""
        else:
            subject_words =  subject_words[0]


        light_words = re.findall(
            r"\s*\**\s*\"*[Ll][Ii][Gg][Hh][Tt][ _][Ww][Oo][Rr][Dd][Ss]\"*\s*\**\s*:\s*\**\s*\"*\s*\"*([^*\n\"]+)",
            response["response"])
        if len(light_words) == 0:
            light_words = ""
        else:
            light_words =  light_words[0]


        environment_words = re.findall(
            r"\s*\**\s*\"*[Ee][Nn][Vv][Ii][Rr][Oo][Nn][Mm][Ee][Nn][Tt][ _][Ww][Oo][Rr][Dd][Ss]\"*\s*\**\s*:\s*\**\s*\"*\s*\"*([^*\n\"]+)",
            response["response"])
        if len(environment_words) == 0:
            environment_words = ""
        else:
            environment_words =  environment_words[0]



        corresponding_prompt["description"] = description
        corresponding_prompt["long_prompt"] = long_prompt
        # corresponding_prompt["main_color_word"] = main_color_word
        corresponding_prompt["camera_angle_word"] = camera_angle_word
        corresponding_prompt["style_words"] = style_words
        corresponding_prompt["subject_words"] = subject_words
        corresponding_prompt["light_words"] = light_words
        corresponding_prompt["environment_words"] = environment_words

        main_components= ["description", "long_prompt", "main_color_word", "camera_angle_word", "style_words", "subject_words", "light_words", "environment_words"]

        full_responses = []
        if "description" in main_components:
            if corresponding_prompt["description"] != "":
                full_responses.append(f"({corresponding_prompt['description']})")
        if "long_prompt" in main_components:
            if corresponding_prompt["long_prompt"] != "":
                full_responses.append(f"({corresponding_prompt['long_prompt']})")
        # if "main_color_word" in main_components:
        #     if corresponding_prompt["main_color_word"] != "":
        #         full_responses.append(f"({corresponding_prompt['main_color_word']})")
        if "camera_angle_word" in main_components:
            if corresponding_prompt["camera_angle_word"] != "":
                full_responses.append(f"({corresponding_prompt['camera_angle_word']})")



        if "style_words" in main_components:
            corresponding_prompt["style_words"] = [x.strip() for x in corresponding_prompt["style_words"].split(",") if
                                                   x != ""]
            print(corresponding_prompt["style_words"])
            if len(corresponding_prompt["style_words"]) > 0:
                full_responses.append(f"({', '.join(corresponding_prompt['style_words'])})")


        if "subject_words" in main_components:
            corresponding_prompt["subject_words"] = [x.strip() for x in corresponding_prompt["subject_words"].split(",") if
                                                     x != ""]
            if len(corresponding_prompt["subject_words"]) > 0:
                full_responses.append(f"({', '.join(corresponding_prompt['subject_words'])})")

        if "light_words" in main_components:
            corresponding_prompt["light_words"] = [x.strip() for x in corresponding_prompt["light_words"].split(",") if
                                                   x != ""]
            if len(corresponding_prompt["light_words"]) > 0:
                full_responses.append(f"({', '.join(corresponding_prompt['light_words'])})")

        if "environment_words" in main_components:
            corresponding_prompt["environment_words"] = [x.strip() for x in
                                                         corresponding_prompt["environment_words"].split(",") if x != ""]
            if len(corresponding_prompt["environment_words"]) > 0:
                full_responses.append(f"({', '.join(corresponding_prompt['environment_words'])})")

        full_response = ", ".join(full_responses)


        # 去除换行
        while full_response.find("\n") != -1:
            full_response = full_response.replace("\n", " ")

        # 句号换成逗号
        while full_response.find(".") != -1:
            full_response = full_response.replace(".", ",")

        # 去除分号
        while full_response.find(";") != -1:
            full_response = full_response.replace(";", ",")

        # 去除多余逗号
        while full_response.find(",,") != -1:
            full_response = full_response.replace(",,", ",")
        while full_response.find(", ,") != -1:
            full_response = full_response.replace(", ,", ",")


        high_quality_prompt = "((high quality:1.4), (best quality:1.4), (masterpiece:1.4), (8K resolution), (2k wallpaper))"
        style_presets_prompt = {
            "none": "",
            "high quality": high_quality_prompt,
            "photography": f"{high_quality_prompt}, (RAW photo, best quality), (realistic, photo-realistic:1.2), (bokeh, cinematic shot, dynamic composition, incredibly detailed, sharpen, details, intricate detail, professional lighting, film lighting, 35mm, anamorphic, lightroom, cinematography, bokeh, lens flare, film grain, HDR10, 8K)",
            "illustration": f"{high_quality_prompt}, ((detailed matte painting, intricate detail, splash screen, complementary colors), (detailed),(intricate details),illustration,an extremely delicate and beautiful,ultra-detailed,highres,extremely detailed)",
        }

        if style_categories == "none":
            full_response =  f"{full_response}"
        elif style_categories == "high quality":
            style = style_presets_prompt["high quality"]
            full_response = f"{full_response}, {style}"
        elif style_categories == "photography":
            style = style_presets_prompt["photography"]
            full_response = f"{full_response}, {style}"
        elif style_categories == "illustration":
            style = style_presets_prompt["illustration"]
            full_response = f"{full_response}, {style}"

        return (full_response,response['context'],)

NODE_CLASS_MAPPINGS = {
    "OllamaVision": OllamaVision,
    "OllamaGenerate": OllamaGenerate,
    "OllamaGenerateAdvance": OllamaGenerateAdvance,
    "OllamaSpecialGenerateAdvance": OllamaSpecialGenerateAdvance,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OllamaVision": "My Ollama Vision",
    "OllamaGenerate": "My Ollama Generate",
    "OllamaGenerateAdvance": "My Ollama Generate Advance",
    "OllamaSpecialGenerateAdvance": "My Ollama Special Generate Advance",
}


