# EdgeLLM

## DisCoPilot: Disconnected CoPilot

The devcontainer will setup all dependencies.  Once in, perform the following tasks to configure and build and start the flask API and REACT chatbot front end:

- Add a model under `/models` and update `/edge-api/server-no-embeddings.py` and `/edge-api/server.py` with the model name
- Add an `/uploads` folder under `/edge-api/`
- `cd edge-api` and run `npm install` in terminal
- `cd edge-ui` and run `npm install`in terminal
- Run `make dev` from the root folder in terminal and note the port where the app is running

You can drop files onto the chatbot surface which will create in-memory embeddings which you can reason over.  Restarting the app will recycle the state and you will need to upload new files.

## Running the sample

### IMPORTANT NOTICE CPU/GPU
Within each [/edge-api/server.py]() script, you need to set the number of CPU threads, or GPU layers to use.
 
 - CPU: `n_threads` should be the same as your system
 - GPU: `n_gpu_layers` depends on how much VRAM you have. Is trial and error.

``` python
# CPU only
model = LlamaCpp(model_path="../models/model.gguf", verbose=True, n_threads=8)

# GPU. Only works if you install cuda and install llama-cpp-python with GPU support
model = LlamaCpp(model_path="../models/model.gguf", verbose=True, n_threads=8, n_gpu_layers=20)
```

## Sourcing models
 Check which models are currently supported with Llama.cpp <https://github.com/ggerganov/llama.cpp>, and follow the links to those projects.  
 
 - Download pre-quantised models from Hugging Face <https://huggingface.co/TheBloke>
   - [Llama 2 7B ggml](https://huggingface.co/TheBloke/Llama-2-7B-GGUF) - Download the `llama-2-7b.Q4_K_M.gguf` version into the [/models]() folder