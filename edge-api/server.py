#!pip install Flask
#!pip install langchain llama-cpp-python

from langchain.embeddings import LlamaCppEmbeddings
from flask import Flask
from flask_cors import CORS
from flask import request
from werkzeug.utils import secure_filename
from langchain.document_loaders import TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.llms import LlamaCpp

app = Flask(__name__, static_folder="../edge-ui/dist/", static_url_path="/")
CORS(app)

modelName = "llama-2-7b.Q4_K_M.gguf"
#modelName = "pytorch_model.bin"
model = LlamaCpp(model_path="../models/" + modelName, n_ctx=1024, n_threads=8)
embeddings = LlamaCppEmbeddings(model_path="../models/" + modelName, n_threads=8)

currentDocumentName = ""
currentDocumentPath = ""

qaChain = None

@app.route('/document', methods = ['GET'])
def get_document_details():
    return {
        "name": currentDocumentName
    }

@app.route('/document', methods = ['POST'])
def upload_file():
    
    if len(request.files) == 0:
        return  "nofiles" 
    else:
        print ("files found: ", len(request.files))
    
    currentDocument =  request.files["file"]

    print(currentDocument.filename)
    currentDocumentPath = "./uploads/" + secure_filename(currentDocument.filename)
    print(currentDocumentPath)
    currentDocument.save(currentDocumentPath)

    documents = load_file(currentDocumentPath)

    # From https://python.langchain.com/docs/use_cases/question_answering/how_to/vector_db_qa

    print(documents)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
    print("text was split")
    texts = text_splitter.split_documents(documents)
    
    print(f"Found {len(texts)} chunks")
    
    docSearch = FAISS.from_documents(texts, embeddings)

    print(docSearch)
    # Create a chain that uses the LlamaCPP LLM and FAISS vector store.
    global qaChain 
    # Create a chain that uses the LlamaCPP LLM and FAISS vector store.

    qaChain = RetrievalQA.from_chain_type(llm=model, chain_type="stuff", retriever=docSearch.as_retriever())
    print(qaChain)
    return {"status": "Done"}

@app.route("/prompt", methods=["POST"])
def send_message():
    prompt = request.json["prompt"]
    print("Sending prompt: " + prompt)

    if qaChain is None:
        print("No QA chain")
        response = model(prompt)
        print(response)
        return {
            "prompt": prompt,
            "response": f"I currently don't have any documents loaded, this is what I know so far.\n {response}" # "I'm sorry, I'm not sure how to answer that - I haven't been given a document yet."
        }
    print("Running QA chain")
    response = qaChain.run(prompt)
    
    print(response)

    # return response as json
    return {
        "prompt": prompt,
        "response": response
    }

def load_file(path):
    # if the file extension is .txt, load as text
    if path.endswith(".txt"):
        loader = TextLoader(path)
        documents = loader.load()
    # if the file extension is .pdf, load as pdf
    elif path.endswith(".pdf"):
        loader = PyPDFLoader(path)
        documents = loader.load_and_split()

    return documents

@app.route("/", methods=["GET"])
def index():
    # server up from static folder
    return app.send_static_file("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)