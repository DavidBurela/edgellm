#!pip install langchain llama-cpp-python
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from langchain.llms import LlamaCpp

### Cloud
# model = OpenAI()

### Edge
# model = LlamaCpp(model_path="./models/llama-7b-ggml-v2-q4_0.bin", verbose=True, n_threads=8, n_gpu_layers=26)
# model = LlamaCpp(model_path="./models/stable-vicuna-13B-ggml_q4_0.bin", verbose=True, n_threads=8, n_gpu_layers=10)
#model = LlamaCpp(model_path="./models/llama-2-7b.Q4_K_M.gguf", verbose=True, n_threads=8, n_gpu_layers=26)

model = OpenAI(openai_api_base = "http://localhost:8000/v1", openai_api_key="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=model)
question = "You are a interviewer interviewing a potential candidate for a senior engineer. You need to ascertain if this person is fit for the role by asking a series of questions in order to establish if they understand Azure at a deep technical level.  Please ask 5 questions that the interviewer can ask. "

response=llm_chain.run(question)
print("Response: " + response)

#python -m llama_cpp.server --model ./models/llama-2-7b.Q4_K_M.gguf --n_threads=4 --n_gpu_layers 20
