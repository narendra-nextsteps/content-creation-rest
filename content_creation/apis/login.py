from flask_restful import Resource
from content_creation import flask_request_response
from content_creation_db.api_queries.login import login_query_response

POST_REQUEST = "POST"
LOGIN_API = "/login"


class Login(Resource):
    def post(self):
        json_req = flask_request_response.json_request(LOGIN_API, POST_REQUEST)

        try:
            query_response = login_query_response(
                json_req['user_id'], json_req['password'])
            return query_response

        except Exception as err:
            return flask_request_response.error_response(
                str(err), LOGIN_API, POST_REQUEST
            )
