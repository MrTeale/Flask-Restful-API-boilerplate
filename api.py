# using https://flask-restful.readthedocs.io/en/latest/installation.html#installation
# https://flask-restful.readthedocs.io/en/latest/quickstart.html
from flask import Flask
from flask_restful import reqparse, Api, Resource
from src.config import config
from src.database import database
from src.auth import authentication as auth

# import YOUR_FILE_HERE

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('email')
parser.add_argument('password')
parser.add_argument('variable')  # replace variable with your variable name

class API(Resource):

    def post(self):
        args = parser.parse_args()
        print(args)
        email = args['email']
        password = args['password']

        config()
        database()
        auth(email, password)

        # call your functions here
        return args, 200

#
# Actually setup the Api resource routing here
#
api.add_resource(API, '/api')


if __name__ == '__main__':
    app.run(debug=True)
