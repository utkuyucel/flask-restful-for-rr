from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from dev_value import Calculate

app = Flask(__name__)
api = Api(app)


class Out(Resource):
	def get(self):
		return {"about":"This is a Rest API Server for calculating the optimal value !"}

	def post(self):
		jjon = request.get_json()
		return {"sent:", jjon}, 201


class Multi(Resource):
	def get(self, num):
		calculate = Calculate(num, 3500, 4)._run()
		return jsonify({"value":calculate})

api.add_resource(Out, "/")
api.add_resource(Multi, "/rr/<float:num>")


if __name__ == "__main__":
	app.run(debug = True)