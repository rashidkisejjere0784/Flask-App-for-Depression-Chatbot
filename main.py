from flask import Flask, request, jsonify
from aitextgen import aitextgen

app = Flask(__name__)
Model = aitextgen(model_folder="pytorch")

@app.route("/")
def index():
    return "hello from Therapp Chat"

@app.route("/predict", methods = ["POST"])
def predict():
    content = request.json
    text = content['text']
    generated_text = Model.generate_one(prompt=text)
    result = {"output" : generated_text}

    return jsonify(result)

app.run(debug=True)

