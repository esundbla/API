from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

data = {"date": "12/27/2023",
        "value": 1465.7}

# /data
class Data(Resource):
    def get(self):
        return data, 200

api.add_resource(Data, '/data')


if __name__ == "__main__":
    app.run(debug=True)
