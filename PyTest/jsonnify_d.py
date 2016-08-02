# coding=utf-8
from flask import Flask, json, jsonify, Response
app = Flask(__name__)


@app.route('/')
def index():
	data = [{'k':'v','ka':'va','o':u'天'},
	{'kv':'vv','kav':'vav','o':u'天'}]
	a = json.dumps(data)
	# b = jsonify(data)
	print a
	return Response(json.dumps(a),  mimetype='application/json')

def main():
	app.run(debug=True, port=8181)


if __name__ == '__main__':
	main()