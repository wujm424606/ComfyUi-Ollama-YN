## Language

- [English](#english)
- [中文](#中文)

---

### English

## Update

5/15/2024 Add keep_alive support
7/15/2024 Add extra model name which it can be added by users.

0 means releasing the video memory immediately after loading the model, while 60m represents that the model will not be released from the video memory until 60m has passed since it was loaded.

# ComfyUi-Ollama-YN
This is just an integrated project. I refer to the ComfyUI-Prompt-MZ project prompt word template setup and comfyui-ollama project to make the prompt word generation more consistent with the requirements of stable diffusion

The projects which I referenced are 

https://github.com/stavsap/comfyui-ollama

https://github.com/MinusZoneAI/ComfyUI-Prompt-MZ

I would like to express my special thanks to the authors of these two projects

# INSTALLATION

1、Install ComfyUI

2、git clone in the custom_nodes folder inside your ComfyUI installation or download as zip and unzip the contents to custom_nodes/ComfyUi-Ollama-YN.
The git git command is git clone https://github.com/wujm424606/ComfyUi-Ollama-YN.git

3、Start/restart ComfyUI

# This section describes how to install ollama

https://ollama.com/

You can download and install ollama from this website

# This section describes how to install models

1、You can choose models by https://ollama.com/library/llama3:8b-instruct-q4_K_M website

2、Input such as ollama run llama3:8b-instruct-q4_K_M in CMD in any folders

![image](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/284ea779-3112-456e-bc1a-2ecd67c60021)



# Let me introduce you to the functionality of this project.

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


# Tips:

If you get an error that says there is no model, install the model as described above

This project involves installing model commands in CMD

1、ollama run llama3:8b-instruct-q4_K_M

2、ollama run llama3

3、ollama run phi3

4、ollama run phi3:3.8b-mini-instruct-4k-q4_K_M

5、ollama run phi3:3.8b-mini-instruct-4k-fp16

6、ollama run llava



---

### 中文

## 更新

5/15/2024 加入keep_alive支持
7/24/2024 加入extra_model支持，使用者可以根据自己想要加载的模型再里面填写，当extra_model不为none，将根据extra_model进行加载模型

0为加载模型后即释放显存，60m代表模型在显存内存在60m后才会释放

# ComfyUi-Ollama-YN
这是一个整合的项目，我在comfyui-ollama 项目的基础上参考了 ComfyUI-Prompt-MZ 项目的提示词和正则代码使生成的提示词更符合stable diffusion的格式

参考的两个项目是

https://github.com/stavsap/comfyui-ollama

https://github.com/MinusZoneAI/ComfyUI-Prompt-MZ


在这里我向这两个项目的作者表示由衷的感谢

# 安装
1、安装ComfyUI

2、在custom_nodes 文件夹下在cmd页面输入git clone https://github.com/wujm424606/ComfyUi-Ollama-YN.git 完成项目的安装 或者 下载zip文件将文件解压到custom_nodes/ComfyUi-Ollama-YN目录


3、重启ComfyUI

# 安装Ollama

https://ollama.com/

![image](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/6c057ba6-4483-40a6-b7cd-28eeca9ff128)


点开上面的网址，然后点击下载，然后进行安装即可

# 通过ollama安装模型

0、模型安装的默认位置是C盘的用户文件夹下的.ollama文件夹里，这个下载目录可以通过设置全局变量进行修改，修改方法参考
https://blog.csdn.net/Yurixu/article/details/136443395

1、安装完ollama后在后台中需要将ollama保持启动状态

![image](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/b0851265-1bc2-4f24-97a8-36fb296e6888)

2、点开 https://ollama.com/library 网站，搜索然后选择好要安装的模型
例如![image](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/ea0468f7-b150-4a12-a61d-daf94c1ddd22)

3、然后在任意文件夹里面调出cmd页面，输入ollama run llama3:8b-instruct-q4_K_M
![image](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/4c019e9b-85d8-407c-9c9b-4b9dfecfa056)

4、安装完成后关闭cmd页面即可

# 主要功能
功能一:
![图片提示词推导](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/4792f5f0-27ea-4e82-8dc1-fe54cbb0dbc4)
这个功能是推导图片的提示词

![image](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/7fe2a2b8-2b00-4388-becc-4646dca849c6)

这个默认模型是 llava模型。如果你有更好的模型，可以在安装好新模型后，在原有模型名字文字修改成新模型的名字，即可以调用

功能二:

![简单问答](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/21c8be5a-6470-4063-8a8a-3d787dadff82)

这个功能是简单问答功能

![image](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/86021a02-b67f-4e8b-a759-96858cd5311b)


这个默认模型是 llama3模型。如果你有更好的模型，可以在安装好新模型后，在原有模型名字文字修改成新模型的名字，即可以调用

功能三:

![提示词润色](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/252d3f32-7d4f-4df3-81a2-27a75f74fd58)

这个功能是根据文本进行提示词润色

功能四:

![上下文联系问答](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/5007aa0f-1cef-42a6-8b98-fc94c529eb71)

这个功能是通过联系上文进行问答功能


功能五：


![生成更符合stable diffusion的提示词](https://github.com/wujm424606/ComfyUi-Ollama-YN/assets/38379474/0981b60b-64f6-4840-9e02-d16f67041718)

这个功能是根据输入生成更符合stable diffusion格式的提示词


# 提示:

如果你的后台出现没有模型的错误，请参考上面选择对应的模型进行安装

这是这个项目中涉及的安装的模型的运行命令

1、ollama run llama3:8b-instruct-q4_K_M

2、ollama run llama3

3、ollama run phi3

4、ollama run phi3:3.8b-mini-instruct-4k-q4_K_M

5、ollama run phi3:3.8b-mini-instruct-4k-fp16

6、ollama run llava






