from flask import Flask, jsonify
import re
from flask import request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__)

app.json_encoder = LazyJSONEncoder

swagger_template = {
	"swagger":"2.0",
	"info":{
		"title": "API Documentation for Data Processing and Modelling",
		"description": "Dokumentasi API untuk Data Processing dan Modelling",
		"version": "1.0.0"
	}
}

swagger_config = {
	"headers" : [],
	"specs" : [
		{
			"endpoint" : 'docs',
			"route" : '/docs.json'
		}
	],
	"static_url_path" : '/flasgger_statis',
	"swagger_ui" : True,
	"specs_route" : "/docs/"
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)

@swag_from("./docs/hello_world.yml", methods=['GET'])
@app.route('/', methods=['GET'])
def hello_world():
	json_response = {
		'status_code' : 200,
		'description' : "Menyapa Hello World",
		'data' : "Hellow World",
	}
	response_data = jsonify(json_response)
	return response_data

@app.route('/text', methods=['GET'])
def text():
	json_response = {
		'status_code' : 200,
		'description' : "Original text",
		'data' : "Hellow, apa kabar semua?",
	}
	response_data = jsonify(json_response)
	return response_data

@app.route('/text-clean', methods=['GET'])
def text_clean():
	json_response = {
		'status_code' : 200,
		'description' : "Original text",
		'data' : re.sub(r'[^a-zA-Z0-9]', '', "Hellow, apa kabar semua9999?"),
	}
	response_data = jsonify(json_response)
	return response_data


if __name__ == '__main__':
	app.run()