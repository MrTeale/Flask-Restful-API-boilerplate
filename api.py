# using https://flask-restful.readthedocs.io/en/latest/installation.html#installation
# https://flask-restful.readthedocs.io/en/latest/quickstart.html
from flask import Flask
from flask_restful import reqparse, Api, Resource
from src.config import config
from src.database import database, save_data_customKey
from src.auth import authentication as auth
from src.user import create_user as create, refresh_user_token as refresh, get_info

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('email')
parser.add_argument('password')
parser.add_argument('childName')
parser.add_argument('dataValue')
parser.add_argument('keyName')

class auth(Resource):
    def get(self):
        args = parser.parse_args()
        print(args)

        return auth(args['email'], args['password']), 200

class user(Resource):

    def get(self):
        args = parser.parse_args()
        print(args)

        return get_info(args['email'], args['password'])

    def post(self):
        args = parser.parse_args()
        print(args)

        return create(args['email'], args['password']), 201

    def patch(self):
        args = parser.parse_args()
        print(args)

        return refresh(args['email'], args['password']), 200

class database(Resource):

    def get(self):
        args = parser.parse_args()
        print(args)
        return save_data_customKey(args['keyName'], args['dataValue'], args['childName']), 200

    def post(self):
        args = parser.parse_args()
        print(args)
        return save_data_customKey(args['keyName'], args['dataValue'], args['childName']), 201

#
# Actually setup the Api resource routing here
#
api.add_resource(auth, '/auth')
api.add_resource(user, '/user')
api.add_resource(database, '/database')


if __name__ == '__main__':
    app.run(debug=True)
