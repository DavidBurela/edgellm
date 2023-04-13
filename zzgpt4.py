# pip install pyllamacpp
from langchain.llms import GPT4All

# Instantiate the model
model = GPT4All(model="/home/david/source/playground/llama.cpp/models/gpt4all-7B/gpt4all-lora-quantized-new.bin", n_ctx=512, n_threads=8)

# Generate text
prompt = "Once upon a time, "

print("Sending prompt: " + prompt)
response = model(prompt)
print(response)