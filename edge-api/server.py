#!pip install Flask
#!pip install langchain llama-cpp-python

from langchain.llms import LlamaCppEmbeddings
from flask import Flask
from flask_cors import CORS
from flask import request
from werkzeug import secure_filename
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma

app = Flask(__name__)
CORS(app)

currentDocumentName = ""
currentDocumentPath = ""
qaChain = None

model = LlamaCppEmbeddings(model_path="../models/llama-2-7b.Q4_K_M.gguf", n_threads=17)

@app.route('/document', methods = ['GET'])
def get_document_details():
    return {
        "name": currentDocumentName
    }

@app.route('/document', methods = ['POST'])
def upload_file():
    if len(request.files) == 0:
        return   
    
    currentDocumentName =  request.files.keys[0]
    f = request.files[currentDocumentName]
    currentDocumentPath = secure_filename(f.filename)
    f.save(currentDocumentPath)

    # From https://python.langchain.com/docs/use_cases/question_answering/how_to/vector_db_qa

    loader = TextLoader(currentDocumentPath)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
    texts = text_splitter.split_documents(documents)
    print(f"{len(texts)} chunks")
    
    docSearch = Chroma.from_documents(texts, model)

    # Create a chain that uses the OpenAI LLM and HNSWLib vector store.
    qaChain = RetrievalQA.from_chain_type(llm=model, chain_type="stuff", retriever=docSearch.as_retriever())


@app.route("/prompt", methods=["POST"])
def send_message():
    prompt = request.json["prompt"]
    print("Sending prompt: " + prompt)

    if qaChain is None:
        return {
            "prompt": prompt,
            "response": "I'm sorry, I'm not sure how to answer that - I haven't been given a document yet."
        }

    response = qaChain.run(prompt)
    
    print(response)

    # return response as json
    return {
        "prompt": prompt,
        "response": response
    }

# serve the ui from static files
@app.route("/")
def index():
    return app.send_from_directory("../edge-ui/dist", "index.html")
