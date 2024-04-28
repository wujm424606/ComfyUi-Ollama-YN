# ComfyUi-Ollama-YN
This is just an integrated project. I refer to the ComfyUI-Prompt-MZ project prompt word template setup based on the comfyui-ollama project to make the prompt word generation more consistent with the requirements of stable diffusion

The projects which I referenced are 

https://github.com/stavsap/comfyui-ollama

https://github.com/MinusZoneAI/ComfyUI-Prompt-MZ

I would like to express my special thanks to the authors of these two projects

INSTALLATION
1、Install ComfyUI

2、git clone in the custom_nodes folder inside your ComfyUI installation or download as zip and unzip the contents to custom_nodes/ComfyUi-Ollama-YN.
The git git command is 

3、Start/restart ComfyUI


Let me introduce you to the functionality of this project.

First function:
![图片提示词推导](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/4792f5f0-27ea-4e82-8dc1-fe54cbb0dbc4)
This function is to deduce the prompt words according to the picture

![image](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/7fe2a2b8-2b00-4388-becc-4646dca849c6)

The default modle is llava model. If you have a better model, you can change the model by changing the model name

Second function:

![简单问答](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/21c8be5a-6470-4063-8a8a-3d787dadff82)

This function is a simple question and answer function.

![image](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/86021a02-b67f-4e8b-a759-96858cd5311b)


The default modle is llama3 model. If you have a better model, you can change the model by changing the model name

Third function:

![提示词润色](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/252d3f32-7d4f-4df3-81a2-27a75f74fd58)

This function allows the model to be embellished according to your prompt words

Four function:

![上下文联系问答](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/5007aa0f-1cef-42a6-8b98-fc94c529eb71)

This function is to answer questions by contacting above

Five function：


![生成更符合stable diffusion的提示词](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/0981b60b-64f6-4840-9e02-d16f67041718)

This function is to generate prompt words that more closely follow the stable diffusion pattern

