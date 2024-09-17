// mport { app } from "../../../../web/scripts/app.js";
import { app } from "/scripts/app.js";

app.registerExtension({
    name: "Comfy.ollamaCommand",
    // 在注册节点之前执行
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        const fetchModels = async (url) => {
            try {
              const response = await fetch("/ollama-YN/get_current_models", {
                method: "POST",
                headers: {
                  "Content-Type": "application/json",
                },
                body: JSON.stringify({
                  url,
                }),
              });

              if (response.ok) {
                const models = await response.json();
                console.debug("Fetched models:", models);
                return models;
              } else {
                console.error(`Failed to fetch models: ${response.status}`);
                return [];
              }
            } catch (error) {
              console.error(`Error fetching models`, error);
              return [];
            }
        };

        const dummy = async () => {
          // calling async method will update the widgets with actual value from the browser and not the default from Node definition.
        }


        if (["MyOllamaGenerate", "MyOllamaGenerateAdvance", "MyOllamaSpecialGenerateAdvance"].includes(nodeData.name) ) {
          const originalNodeCreated = nodeType.prototype.onNodeCreated;
          nodeType.prototype.onNodeCreated = async function () {
            if (originalNodeCreated) {
              originalNodeCreated.apply(this, arguments);
            }

            const urlWidget = this.widgets.find((w) => w.name === "url");
            const modelWidget = this.widgets.find((w) => w.name === "model");
            const updateModels = async () => {
              const url = urlWidget.value;
              const prevValue = modelWidget.value
              modelWidget.value = ''
              modelWidget.options.values = []

              var models = await fetchModels(url);

              const text_signal ="(text)"
              models = models.filter(model => model.includes(text_signal))

              var add_text_models = ["llama3.1:latest (text)", "llama3:latest (text)", "qwen2:latest (text)",
                "phi3.5:latest (text)", "phi3:latest (text)", "trollek/qwen2-diffusion-prompter:latest (text)"]
              add_text_models.forEach(model => {
                if (!models.includes(model)) {
                  models.unshift(model);}
              });

              // Update modelWidget options and value
              modelWidget.options.values = models;
              console.debug("Updated text modelWidget.options.values:", modelWidget.options.values);

              if (models.includes(prevValue)) {
                modelWidget.value = prevValue; // stay on current.
              } else if (models.length > 0) {
                modelWidget.value = models[0]; // set first as default.
              }

              console.debug("Updated text modelWidget.value:", modelWidget.value);
            };



        // Initial update
            await dummy(); //

            await updateModels();
          };

      } else if (["MyOllamaVision"].includes(nodeData.name) ) {
          const originalNodeCreated = nodeType.prototype.onNodeCreated;
          nodeType.prototype.onNodeCreated = async function () {
            if (originalNodeCreated) {
              originalNodeCreated.apply(this, arguments);
            }

            const urlWidget = this.widgets.find((w) => w.name === "url");
            const modelWidget = this.widgets.find((w) => w.name === "model");
            const updateModels = async () => {
              const url = urlWidget.value;
              const prevValue = modelWidget.value
              modelWidget.value = ''
              modelWidget.options.values = []

              var models = await fetchModels(url);


              const vision_signal ="(vision)"
              models = models.filter(model => model.includes(vision_signal))


              var add_vision_models = ["mskimomadto/chat-gph-vision:latest (vision)", "moondream:latest (vision)", "llava:latest (vision)",
               "minicpm-v:latest (vision)"]
              add_vision_models.forEach(model => {
                if (!models.includes(model)) {
                  models.unshift(model);}
              });

              // Update modelWidget options and value
              modelWidget.options.values = models;
              console.debug("Updated vision modelWidget.options.values:", modelWidget.options.values);

              if (models.includes(prevValue)) {
                modelWidget.value = prevValue; // stay on current.
              } else if (models.length > 0) {
                modelWidget.value = models[0]; // set first as default.
              }

              console.debug("Updated vision modelWidget.value:", modelWidget.value);
            };


        // Initial update
            await dummy(); //
            await updateModels();
          };
      } else if (["MyOllamaDeleteModel"].includes(nodeData.name) ) {
          const originalNodeCreated = nodeType.prototype.onNodeCreated;
          nodeType.prototype.onNodeCreated = async function () {
            if (originalNodeCreated) {
              originalNodeCreated.apply(this, arguments);
            }

            const urlWidget = this.widgets.find((w) => w.name === "url");
            const modelWidget = this.widgets.find((w) => w.name === "model");
            const updateModels = async () => {
              const url = urlWidget.value;
              const prevValue = modelWidget.value
              modelWidget.value = ''
              modelWidget.options.values = []

              var models = await fetchModels(url);

              // Update modelWidget options and value
              modelWidget.options.values = models;
              console.debug("Delete modelWidget.options.values:", modelWidget.options.values);

              if (models.includes(prevValue)) {
                modelWidget.value = prevValue; // stay on current.
              } else if (models.length > 0) {
                modelWidget.value = models[0]; // set first as default.
              }

              console.debug("Delete modelWidget.value:", modelWidget.value);
            };

            // Initial update
            await dummy(); //
            await updateModels();
          };
      }
    },
});
