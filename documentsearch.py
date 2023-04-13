# pip install tiktoken faiss-cpu
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import LlamaCppEmbeddings

loader = TextLoader('data/codereviewer.txt')
documents = loader.load()

# Split your docs into texts
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
texts = text_splitter.split_documents(documents)

# Get embedding engine ready
embeddings = OpenAIEmbeddings()
# embeddings = LlamaCppEmbeddings(model_path="./models/gpt4all-lora-quantized-new.bin")

# Embedd your texts
db = FAISS.from_documents(texts, embeddings)
retriever = db.as_retriever()

print(retriever)
docs = retriever.get_relevant_documents("race conditions")
for doc in docs:
    print("###")
    print(doc.page_content[:200])