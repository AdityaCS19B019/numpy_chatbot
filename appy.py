from flask import Flask, jsonify, request
from flask_cors import CORS
#from sample import search_stackoverflow
from chat import get_response, bot_name
from flask import render_template

app = Flask(__name__)
CORS(app)

@app.route("/")
def welcome():
    return f"Welcome to numpy api!"

@app.route("/<msg>", methods = ['POST', 'GET'])
def response(msg):
    if request.method == 'GET':
        return f"Response :- {get_response(msg)}"
    else:
        return jsonify(result = get_response(msg))



if __name__ == "__main__":
  app.run()