#!pip install langchain transformers llama-cpp-python

from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

### Cloud
# model = OpenAI(temperature=0)

### Edge
from langchain.llms import LlamaCpp
# model = LlamaCpp(model_path="./models/gpt4all-lora-quantized-new.bin", n_ctx=2048, verbose=True, n_threads=16)
# model = LlamaCpp(model_path="./models/ggml-vicuna-7b-4bit-rev1.bin", n_ctx=2048, verbose=True, n_threads=16)
model = LlamaCpp(model_path="./models/ggml-vicuna-13b-4bit-rev1.bin", n_ctx=4096, verbose=True, n_threads=16, max_tokens=1024)

loader = TextLoader('data/codereviewer.txt')
documents = loader.load()

# Get your splitter ready
text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)

# Split your docs into texts
texts = text_splitter.split_documents(documents[:3])

chain = load_summarize_chain(model, chain_type="refine", verbose=True)
result = chain.run(texts)
print(result)