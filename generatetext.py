#!pip install langchain llama-cpp-python
from langchain.llms import OpenAI
from langchain.llms import LlamaCpp

## Cloud
# model = OpenAI()

### Edge
model = LlamaCpp(model_path="./models/llama-2-7b.Q4_K_M.gguf", verbose=True, n_threads=8, n_gpu_layers=26)
# model = LlamaCpp(model_path="./models/stable-vicuna-13B-ggml_q4_0.bin", verbose=True, n_threads=8, n_gpu_layers=10)
#model = LlamaCpp(model_path="./models/koala-7B.ggml.q4_0.bin", verbose=True, n_threads=8, n_gpu_layers=26)

# Generate text
prompt = "You are a interviewer interviewing a potential candidate for a senior engineer. You need to ascertain if this person is fit for the role by asking a series of questions in order to establish if they understand Azure at a deep technical level.  Please ask 5 questions that the interviewer can ask. "

print("Sending prompt: " + prompt)
response = model(prompt)
print(response)

