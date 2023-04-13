#!pip install langchain llama-cpp-python
from langchain import PromptTemplate, LLMChain
from langchain import OpenAI
from langchain.llms import LlamaCpp

### Cloud
model = OpenAI()

### Edge
model = LlamaCpp(model_path="./models/gpt4all-lora-quantized-new.bin", verbose=True, n_threads=16)
# model = LlamaCpp(model_path="./models/ggml-vicuna-7b-4bit-rev1.bin", verbose=True, n_threads=16)
# model = LlamaCpp(model_path="./models/ggml-vicuna-13b-4bit-rev1.bin", verbose=True, n_threads=16)


template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=model)
question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

response=llm_chain.run(question)
print("Response: " + response)