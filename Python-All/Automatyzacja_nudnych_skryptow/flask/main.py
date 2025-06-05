from flask_restful import Resource, Api
from flask import Flask

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World!"}


if __name__ == "__main__":
    api.add_resource(HelloWorld, "/helloworld")
    app.run(host="127.0.0.1", port=8822, debug=True)

    api.get()
