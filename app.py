from flask import Flask, request, render_template, jsonify
import json


app = Flask(__name__)

# Load responses from JSON file
with open('data/responses.json') as f:
    responses = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"].strip().lower()
    response = responses.get(user_input, responses["default"])
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

