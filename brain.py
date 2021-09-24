#brain of this whole useless FrontEnd
#you got here? Please ask me if I like pasztetowa in our next conversation ;)

#initialize Flask API
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast




app = Flask(__name__)
api = Api(app)

class SendMessage(Resource):

    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('username', required=True)  # add args
        parser.add_argument('message', required=True)
        
        args = parser.parse_args()  # parse arguments to dictionary
        
        # create new dataframe containing new values
        new_data = pd.DataFrame({
            'username': args['username'],
            'message': args['message'],
            'locations': [[]]
        })
        # read our CSV
        data = pd.read_csv('users.csv')
        # add the newly provided values
        data = data.append(new_data, ignore_index=True)
        # save back to CSV
        data.to_csv('users.csv', index=False)
        return {'data': data.to_dict()}, 200  # return data with 200 OK

class Messages(Resource):
    @app.route("/", methods=["GET"])
    def get(self):
        data = pd.read_csv('users.csv')
        data = data.to_dict()
        response = jsonify(message=data)
        response.headers.add("Access-Control-Allow-Origin","*") #bez tego występuje problem CORS missing allow origin
        response.headers.add("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        return response

api.add_resource(SendMessage, '/send_message')  # '/users' is our entry point
api.add_resource(Messages, '/get_messages')


if __name__ == '__main__':
    app.run()  # run our Flask app
 