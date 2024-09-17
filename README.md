## Language

- [English](#english)
- [中文](#中文)

---

### English

## Update

9/17/2024 I made a major update that adjusted the way we download models and load display models, and also provided the ability to delete download models and save load contexts, Please read the whole Readme file.

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

1、You can choose models by https://ollama.com/brxce/stable-diffusion-prompt-generator

2、Input model name in the extra model and run

![DownLoad New Model Workflow](https://github.com/user-attachments/assets/9ffa6a7e-cc9b-4121-ac0f-c9093854b37c)


Detailed information be shown in the Tips.



# Let me introduce you to the functionality of this project.

First function:

![My Ollama Vision WorkFlow](https://github.com/user-attachments/assets/ca161d03-f7f2-418f-84a3-d1ee3ef34493)


This function is to deduce the prompt words according to the picture

![image](https://github.com/user-attachments/assets/9939256e-423e-4bc6-accd-b9afb92a5fa9)


I provide 4 default vision models.  If you have a better model, you can add new model in the extra model. Click Run and it will automatically download the model.
When downloading the model is completed, search and load the node again, and the newly downloaded model will be automatically loaded into the model list.

Second function:

![My Ollama Generate WorkFlow](https://github.com/user-attachments/assets/ffa537ee-7113-41c4-ba9b-dbb8fae3380b)


This function is a simple question and answer function.

![image](https://github.com/user-attachments/assets/34d184a6-753d-477e-b9d6-0341d43fdba7)



I provide 6 default text models.  If you have a better model, you can add new model in the extra model. Click Run and it will automatically download the model.
When downloading the model is completed, search and load the node again, and the newly downloaded model will be automatically loaded into the model list.


Third function:

![Ollama Generate Advance WorkFlow](https://github.com/user-attachments/assets/d421e4dd-5550-455c-83a8-590c788339a1)


This function allows the model to be embellished according to your prompt words

Four function:

![My Ollama Generate Advance WorkFlow-Context](https://github.com/user-attachments/assets/b569c912-d9c7-44c4-82ac-19f2afe38f60)


This function is to answer questions by contacting above

Five function:


![Equal My Ollama Generate WorkFlow](https://github.com/user-attachments/assets/c8a81fe1-9401-470e-a318-b2e6e86c2de9)


This function is to answers the question by loading the previously saved context


Six function：


![My Ollama Special Generate Advance WorkFlow](https://github.com/user-attachments/assets/ba58906f-3752-4f0f-b379-814aada24f6e)


This function is to generate prompt words that more closely follow the stable diffusion pattern

Seven function：


![My Ollama Delete Model WorkFlow](https://github.com/user-attachments/assets/c41e5a28-0396-4f54-bf33-bd986b8ad609)


This function is to delete model which we downloaded.


# Tips:

1、

Before：

This is how to download models before updating:

This project involves installing model commands in CMD

ollama run model_name

Now:

We can download model in the extra model by input model name.

![DownLoad New Model Workflow](https://github.com/user-attachments/assets/68eb518d-00be-4d6c-b6df-c1d5bfa1fef4)


And the downloading process will be shown in the cmd：

This is a sign picture of a successful download completion


<img width="418" alt="download" src="https://github.com/user-attachments/assets/8c31d9de-7687-43f7-b11d-9d229778f9ce">



2、 If you previously had download models and now want to display them in the load list

  1、 first you can input "ollama list" in the cmd
    
<img width="831" alt="显示ollama list" src="https://github.com/user-attachments/assets/d9375695-e56c-466a-a8a1-eb0ba77cabee">
    
  2、 then, you find the category.csv file in the ComfyUi-Ollama-YN\file and open it by excel or other tools.
    
 <img width="290" alt="excel1" src="https://github.com/user-attachments/assets/c46b5411-da74-41f2-b9fd-ae65f2343421">
    
  3、 Fill in the name of the model you found under the ollama list command into the two columns of the csv file. Whether the model is filled in vision_model or text_model can be judged based on the model 
    description on the ollama website. The visual model is the back-deduced, and the text model can answer questions.
    
  <img width="462" alt="excel2" src="https://github.com/user-attachments/assets/7f8ac70b-f7b0-42f9-802f-39c5956ff989">
    
  4、 Save the csv file and open the comfyui， you can see the models you downloaded
    
  <img width="385" alt="text模型名" src="https://github.com/user-attachments/assets/85c48a4c-30d7-477f-b3ee-c5e1787f1ecd">
    
 <img width="385" alt="text模型名" src="https://github.com/user-attachments/assets/5c7a14a9-8b70-441a-84e4-f7c91fa67cf5">
    


3、 When we find the model to download on the Ollama official website, if the model name after run does not have the: annotation parameter, it will automatically mark latest when downloading, so we need to manually add ":latest" after the model name to download this type of model in the extra model

  <img width="648" alt="注意" src="https://github.com/user-attachments/assets/c408f47c-c1ed-454d-9e87-71d18e1e505f">
  
  <img width="621" alt="注意2" src="https://github.com/user-attachments/assets/96c85f19-240a-4dc2-8f5a-fce1779d6bf3">
  
  <img width="508" alt="注意3" src="https://github.com/user-attachments/assets/8f9d87fd-548e-4312-b8c8-1900da84cbc6">
  


4、 After we download the model, we need to search and import it again, and the newly downloaded model will be displayed in the model list. However, don't use the right mouse button to directly reload the model, which will cause an error.
   The correct way is as follows:
   
   <img width="705" alt="正确方式" src="https://github.com/user-attachments/assets/d24656b1-f91e-418d-b718-1e78f7962c81">
   
   <img width="423" alt="注意4png" src="https://github.com/user-attachments/assets/72ee4398-2482-4baa-8538-9fbde113de9e">
   

   The wrong way is as follow:
   
   <img width="482" alt="错误方式" src="https://github.com/user-attachments/assets/37f9b8a4-ae79-458e-8a10-884c2cad3402">
   

5、Use the save context node to save the context into a file. If you use the load context node to load it at this time, the file will not be displayed. You need to restart comfyui to find the file



   







   
    

    
    




---

### 中文

## 更新


9/17/2024 我对这个现有的ollama项目进行了一次重大更新，调整了我们下载模型和加载显示模型的方式，还提供了删除下载模型和保存加载上下文的能力，详情请阅读以下文件

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

2、点开 https://ollama.com/library 网站，搜索然后选择好要安装的模型，然后输入模型名在ollama vision或许ollama generate节点的extra model里，点击运行即可完成安装


![DownLoad New Model Workflow](https://github.com/user-attachments/assets/9ffa6a7e-cc9b-4121-ac0f-c9093854b37c)


详情看tips提示



# 介绍整个插件的功能

第一个功能:

![My Ollama Vision WorkFlow](https://github.com/user-attachments/assets/ca161d03-f7f2-418f-84a3-d1ee3ef34493)


这个功能就是推导图片的提示词

![image](https://github.com/user-attachments/assets/9939256e-423e-4bc6-accd-b9afb92a5fa9)


我提供4个默认视觉模型。  如果您有更好的模型，可以在extra model中添加模型名。然后点击运行，系统会自动下载模型。模型下载完成后，再次搜索并加载该节点，新下载的模型会自动加载到模型列表中。


第二个功能:

![My Ollama Generate WorkFlow](https://github.com/user-attachments/assets/ffa537ee-7113-41c4-ba9b-dbb8fae3380b)


这个功能就是简单的问答功能.

![image](https://github.com/user-attachments/assets/34d184a6-753d-477e-b9d6-0341d43fdba7)



我提供了6个默认文本模型。  如果您有更好的模型，可以在extra model中添加新模型名。点击运行，系统会自动下载模型。模型下载完成后，再次搜索并加载该节点，新下载的模型会自动加载到模型列表中。


第三个功能:

![Ollama Generate Advance WorkFlow](https://github.com/user-attachments/assets/d421e4dd-5550-455c-83a8-590c788339a1)


这个功能是可以润色提示词。 添加新模型方式，和前面一致


第四个功能:

![My Ollama Generate Advance WorkFlow-Context](https://github.com/user-attachments/assets/b569c912-d9c7-44c4-82ac-19f2afe38f60)


这个功能是根据上下文联动进行多轮回答。 添加新模型方式，和前面一致

第5个功能:


![Equal My Ollama Generate WorkFlow](https://github.com/user-attachments/assets/c8a81fe1-9401-470e-a318-b2e6e86c2de9)


这个功能是通过加载context文件里的内容进行回答，需要和save context节点配合使用.


第6个功能：


![My Ollama Special Generate Advance WorkFlow](https://github.com/user-attachments/assets/ba58906f-3752-4f0f-b379-814aada24f6e)


这个功能是使用内置模板的方式，使模型生成的提示词格式更接近stable diffusion。但需要注意的是，由于内置了模板，所以会对一些模型无效，所以使用模型的选择上需要谨慎。 添加新模型方式，和前面一致


第7个功能：


![My Ollama Delete Model WorkFlow](https://github.com/user-attachments/assets/c41e5a28-0396-4f54-bf33-bd986b8ad609)


这个功能是删除已经下载的模型


# Tips 提示:

1、

以前：

以前，我们下载模型是通过调用cmd，然后输入如下命令完成下载

ollama run model_name

现在:

现在我们不需要在使用cmd输入命令下载了，直接在extra model输入要下载的模型名即可，但是模型名的输入有需要注意的点，在后面会提到

![DownLoad New Model Workflow](https://github.com/user-attachments/assets/68eb518d-00be-4d6c-b6df-c1d5bfa1fef4)


下载过程会在comfyui的cmd里面显示：

成功下载结果如下图


<img width="418" alt="download" src="https://github.com/user-attachments/assets/8c31d9de-7687-43f7-b11d-9d229778f9ce">



2、如果你以前有下载的模型，但由于新更新导致以前下载模型无法显示在模型列表中，请参考以下方法

  1、 首先打开cmd，并输入ollama list, 显示所有已下载的模型
    
<img width="831" alt="显示ollama list" src="https://github.com/user-attachments/assets/d9375695-e56c-466a-a8a1-eb0ba77cabee">
    
  2、  然后，在ComfyUi-Ollama-YN\文件中找到category.CSV文件，并通过Excel或其他工具打开它。
    
 <img width="290" alt="excel1" src="https://github.com/user-attachments/assets/c46b5411-da74-41f2-b9fd-ae65f2343421">
    
  3、  将您在ollama list命令下找到的模型的名称填写到CSV文件的两列中。可以根据 Olama网站上的描述功能 判断模型是填充在vision_mode还是text_mode中。
  简单来说，视觉模型是反推式的，文本模型可以回答问题
    
  <img width="462" alt="excel2" src="https://github.com/user-attachments/assets/7f8ac70b-f7b0-42f9-802f-39c5956ff989">
    
  4、 保存CSV文件并打开comfyui，调用节点在模型列表里即可看到您下载的模型
    
  <img width="385" alt="text模型名" src="https://github.com/user-attachments/assets/85c48a4c-30d7-477f-b3ee-c5e1787f1ecd">
    
 <img width="385" alt="text模型名" src="https://github.com/user-attachments/assets/5c7a14a9-8b70-441a-84e4-f7c91fa67cf5">
    


3、 当我们在Ollama官方网站上找到要下载的模型时，如果run后面的模型名称没有：+参数的形式，那么下载时会自动标记为最新，所以我们需要在型号名称后手动添加“：latest”才能在extra model中下载该模型

  <img width="648" alt="注意" src="https://github.com/user-attachments/assets/c408f47c-c1ed-454d-9e87-71d18e1e505f">
  
  <img width="621" alt="注意2" src="https://github.com/user-attachments/assets/96c85f19-240a-4dc2-8f5a-fce1779d6bf3">
  
  <img width="508" alt="注意3" src="https://github.com/user-attachments/assets/8f9d87fd-548e-4312-b8c8-1900da84cbc6">
  


4、 当我们下载模型完成后，需要再次搜索并导入，新下载的模型就会显示在模型列表中。但不要使用鼠标右键使用reload重新加载模型，否则会导致错误。
   
   正确方式如下图:
   
   <img width="705" alt="正确方式" src="https://github.com/user-attachments/assets/d24656b1-f91e-418d-b718-1e78f7962c81">
   
   <img width="423" alt="注意4png" src="https://github.com/user-attachments/assets/72ee4398-2482-4baa-8538-9fbde113de9e">
   

   错误方式如下图:
   
   <img width="482" alt="错误方式" src="https://github.com/user-attachments/assets/37f9b8a4-ae79-458e-8a10-884c2cad3402">
   

5、使用保存上下文节点将上下文保存到文件中。如果此时使用加载上下文节点加载，则不会显示该文件。您需要重新启动comfyui才能找到文件





