#!pip install langchain llama-cpp-python
from langchain.llms import OpenAI
from langchain.llms import LlamaCpp

## Cloud
model = OpenAI()

## Edge
# model = LlamaCpp(model_path="./models/gpt4all-lora-quantized-new.bin", verbose=True, n_threads=16)
# model = LlamaCpp(model_path="./models/ggml-vicuna-7b-4bit-rev1.bin", verbose=True, n_threads=16)
# model = LlamaCpp(model_path="./models/ggml-vicuna-13b-4bit-rev1.bin", verbose=True, n_threads=16)


# Generate text
prompt = "Once upon a time, "

print("Sending prompt: " + prompt)
response = model(prompt)
print(response)