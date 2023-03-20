from flask import Flask
from flask_restful import Api, Resource , abort
from flask import Flask, redirect, request, jsonify


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get (self):
        return {'Message' : 'Hello Flask!!!'}
    
class HelloName(Resource):
    def get (self, name):
        return {'Message' : 'Hello {}'.format(name)}
    
    
student = {
    1 : {'FirstName' : 'Samarth', 'lastName' : 'Gupta'},
    2 : {'FirstName' : 'Moksha', 'lastName' : 'Jain'},
    3 : {'FirstName' : 'Rochak', 'lastName' : 'Sharma'}
}

class studentList(Resource):
    def get(self):
        try:
            return student
        except Exception as e:
            df = {
                "Error" : "Something went wrong in studentList's GET method",
                "Error_message" : e
            }
            print("Error : " , e)
            return df

class Student(Resource):
    def get(self,studentId):
        try:
            return student[studentId]
        except Exception as e:
            df = {
                "Error" : "Something went wrong in student's GET method",
                "Error_message" : e
            }
            print("Error : " , e)
            return df
    
    def post(self,studentId):
        try: 
            if studentId in student:
                abort(409, "Member with this id already exists, please change its id")
            student[studentId] = {'FirstName' : request.json['FirstName'], 'lastName' : request.json['lastName']}
            return redirect("/studentList")
        except Exception as e:
            df = {
                "Error" : "Something went wrong in student's POST method",
                "Error_message" : e
            }
            print("Error : " , e)
            return df
    
    def put(self,studentId):
        try:
            if studentId not in student:
                print("Relevant Student details are not found with this credentials")
            student[studentId] = {'FirstName' : request.json['FirstName'], 'lastName' : request.json['lastName']}
            return redirect("/studentList")
        except Exception as e:
            df = {
                "Error" : "Something went wrong in student's PUT method",
                "Error_message" : e
            }
            print("Error : " , e)
            return df
    
    def delete(self,studentId):
        try:
            if studentId not in student:
                print("Relevant Student details are not found with this credentials")
            del student[studentId]
            return redirect("/studentList")
        except Exception as e:
            df = {
                "Error" : "Something went wrong in student's DELETE method",
                "Error_message" : e
            }
            print("Error : " , e)
            return df


api.add_resource(HelloWorld,"/")
api.add_resource(HelloName,"/<string:name>")
api.add_resource(studentList,"/studentList")
api.add_resource(Student,"/student/<int:studentId>")

if __name__ == "__main__":
    app.run()
    
    