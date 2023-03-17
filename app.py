from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get (self):
        return {'Message' : 'Hello Flask!!!'}
    
class HelloName(Resource):
    def get (self, name):
        return {'Message' : 'Hello {}'.format(name)}
    
    
api.add_resource(HelloWorld,"/")
api.add_resource(HelloName,"/<string:name>")

if __name__ == "__main__":
    app.run()