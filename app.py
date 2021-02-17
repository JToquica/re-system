from flask import Flask, request, jsonify
from flask_cors import CORS
import turicreate as tc

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    
    return 'Hello World'

if __name__ == '__main__':
    app.run()
