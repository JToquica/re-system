from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/html')
def hello_world_html():
    return '<h1>Hello, World!</h1>'

@app.route('/json')
def hello_world_json():
    return {"message":"Hello, World!"}

@app.route('/json/list')
def hello_world_json_list():
	data = []
	data.append({"name":"Pedro", "age":24})
	data.append({"name":"Maria", "age":18})
	data.append({"name":"Jose", "age":31})
	return {"data":data}

if __name__ == '__main__':
    app.run()