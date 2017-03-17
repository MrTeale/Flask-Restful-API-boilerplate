# using https://flask-restful.readthedocs.io/en/latest/installation.html#installation
# https://flask-restful.readthedocs.io/en/latest/quickstart.html
from flask import Flask
from flask_restful import reqparse, Api, Resource
import pyrebase
# import YOUR_FILE_HERE

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('email')
parser.add_argument('password')
parser.add_argument('variable')  # replace variable with your variable name

# Firebase Config
# based and built off of https://github.com/thisbejim/Pyrebase

config = {
  "apiKey": "apiKey",  # Replace apiKey with yours
  "authDomain": "projectId.firebaseapp.com",  # Replace projectId with yours
  "databaseURL": "https://databaseName.firebaseio.com",  # Replace databaseName with yours
  "storageBucket": "projectId.appspot.com"  # Replace storageBucket with yours
#  Uncomment line below in order to access as an admin (requires .json file with credentials)
# "serviceAccount": "path/to/serviceAccountCredentials.json"
}

firebase = pyrebase.initialize_app(config)

#Firebase check Auth
def checkAuth():
    args = parser.parse_args()
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password(args["email"], args["password"])
    if user['idToken'] != None:
        #do what you wish with the token here
    else:
        print("ERROR: User is not logged in")

checkAuth()

def Database():
    db = firebase.database()
    users = db.child("YourDatabase").get()
    print(users.val()) # {"Lachlan": {"name": "Lachlan Teale"}}

    #Other options can be found at https://github.com/thisbejim/Pyrebase

Database()

class API(Resource):

    def post(self):
        args = parser.parse_args()
        print(args)

        # call your functions here

        return args, 200

#
# Actually setup the Api resource routing here
#
api.add_resource(API, '/api')


if __name__ == '__main__':
    app.run(debug=True)
