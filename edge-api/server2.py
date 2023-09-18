#!pip install Flask
#!pip install langchain llama-cpp-python

from langchain.llms import OpenAI
from langchain.llms import LlamaCpp
from flask import Flask
from flask_cors import CORS
from flask import request

app = Flask(__name__, static_folder="../edge-ui/dist/", static_url_path="/")
CORS(app)

model = LlamaCpp(model_path="../models/llama-2-7b.Q4_K_M.gguf", verbose=True, n_threads=8, n_gpu_layers=26)


@app.route("/prompt", methods=["POST"])
def send_message():
    prompt = request.json["prompt"]
    print("Sending prompt: " + prompt)
    response = model(prompt)

    #response = "hello test"
    print(response)

    # return response as json
    return {
        "prompt": prompt,
        "response": response
    }


@app.route("/", methods=["GET"])
def index():
    # server up from static folder
    return app.send_static_file("index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)