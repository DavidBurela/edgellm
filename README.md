# EdgeLLM
My spikes looking at patterns that allow you to build applications that can be swapped at runtime to run either in hyperscale (Azure OpenAI), or on edge compute (Llama.cpp). 

The more complex examples (like SQL agent) require a lot of very heavy pip dependencies, so I haven't included a `requirements.txt`. Each python file has roughly the packages it needs to run.

## Running the sample

### IMPORTANT
Within each python script, you need to set the number of CPU threads, or GPU layers to use.
 
 - CPU `n_threads` should be the same as your system
 - `n_gpu_layers` depends on how much VRAM you have. Is trial and error.

``` python
# CPU only
model = LlamaCpp(model_path="./models/model.bin", verbose=True, n_threads=8)

# GPU. Only works if you install cuda and install llama-cpp-python with support
model = LlamaCpp(model_path="./models/model.bin", verbose=True, n_threads=8, n_gpu_layers=20)
```

### Quickest. CPU only

``` bash
# If you haven't used python before, create a standalone "virtual environment" to keep the dependencies self contained
apt install python3-venv
python3 -m venv venv
source ./venv/bin/activate

pip install langchain llama-cpp-python # Any others should be at the top of each py file
python generatetext.py
python questionchain.py
```

### GPU enabled
``` bash
## Install Miniconda
# Get latest installer for your OS https://docs.conda.io/en/latest/miniconda.html
curl -LO https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
bash #start new session, to include conda

## Create a Conda environment and activate it
conda create -n edgellm python=3.11 #enter later python version if needed
conda activate edgellm

## Install cuda toolkit version that matches your GPU drivers
# Full list at https://anaconda.org/nvidia/cuda-toolkit
nvidia-smi #GPU Cuda version in top right
conda install -c "nvidia/label/cuda-12.1.1" cuda-toolkit

## Install python libraries
# Ensure llama-cpp-python installs with cuBLAS support https://github.com/abetlen/llama-cpp-python#installation-with-openblas--cublas--clblast
pip install langchain 
export LLAMA_CUBLAS=1
CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python --no-cache-dir

## Run your scripts
time python question
```

## Sourcing models
The easiest way to get started is to see which models are currently supported with Llama.cpp <https://github.com/ggerganov/llama.cpp>, and follow the links to those projects.
Another is to see what compatible 4bit quantised models are available on Hugging Face <https://huggingface.co/4bit>
