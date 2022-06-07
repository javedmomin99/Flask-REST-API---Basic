from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
class HelloWorld(Resource):
    def get(self):
        return {'data' : 'Hello World'}
class HelloName(Resource):
    def get(self,name):
        return {'data' : f"Hello, {name}"}
class HelloAge(Resource):
    def get(self, name, age):
        return {'data' : f"Hello, {name}, Your Age is {age} years."}
#Calling the Function / Class using API Below :
api.add_resource(HelloWorld, "/helloworld")
# HelloWorld is the class , whenever the URL is added with helloworld, it will fetch for the class "HelloWorld" and perform the function

#Calling the Function / Class using API Below :
api.add_resource(HelloName, "/helloworld/<string:name>")
#<string:name> ---> Pass an Argument in the form of String. For Ex : Javed  --> http://127.0.0.1:5000/helloworld/Javed

#Calling the Function / Class using API Below :
api.add_resource(HelloAge, '/helloworld/<string:name>/<int:age>')
# Passing Argument --- > Pass an Argument in the form of String first followed by Integer. For Ex : Javed & 21 --> http://127.0.0.1:5000/helloworld/Javed/21


if __name__ == "__main__":
    app.run(debug=True)