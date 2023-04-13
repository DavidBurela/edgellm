#!pip install langchain llama-cpp-python
from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain

### Cloud
# model = OpenAI()

### Edge
from langchain.llms import LlamaCpp
model = LlamaCpp(model_path="./models/gpt4all-lora-quantized-new.bin", n_ctx=2048, verbose=True, n_threads=16)
# model = LlamaCpp(model_path="./models/ggml-vicuna-7b-4bit-rev1.bin", n_ctx=2048, verbose=True, n_threads=16)
# model = LlamaCpp(model_path="./models/ggml-vicuna-13b-4bit-rev1.bin", n_ctx=2048, verbose=True, n_threads=16)


template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=model)
question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

response=llm_chain.run(question)
print("Response: " + response)