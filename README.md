# EdgeLLM
My spikes looking at patterns that allow you to build applications that can be swapped at runtime to run either in hyperscale (Azure OpenAI), or on edge compute (Llama.cpp). 

The more complex examples (like SQL agent) require a lot of very heavy pip dependencies, so I haven't included a `requirements.txt`. Each python file has roughly the packages it needs to run.

## Running the sample

``` bash
# If you haven't used python before, create a standalone "virtual environment" to keep the dependencies self contained
apt install python3-venv
python3 -m venv venv
source ./venv/bin/activate

pip install langchain etc etc (should be at the top of each py files)
python generatetext.py
```

## Sourcing models
The easiest way to get started is to see which models are currently supported with Llama.cpp <https://github.com/ggerganov/llama.cpp>, and follow the links to those projects.
Another is to see what compatible 4bit quantised models are available on Hugging Face <https://huggingface.co/4bit>
