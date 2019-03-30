from flask_restful import Resource
from content_creation import flask_request_response
from content_creation_db.api_queries.check_user_id_exists import \
    check_user_id_exists_query_response
from content_creation_db.api_queries.signup import signup_query_response

POST_REQUEST = 'POST'
SIGN_UP_API = '/signup'


class SignUp(Resource):
    def post(self):
        json_req = flask_request_response.json_request(
            SIGN_UP_API, POST_REQUEST)

        # if err is not None:
        #     return flask_request_response.error_response(
        #         err, SIGN_UP_API, POST_REQUEST)

        try:
            does_user_exits = check_user_id_exists_query_response(
                json_req["signup_details"]["user_id"])
            if not does_user_exits:
                sign_up_query_response = signup_query_response(
                    json_req["signup_details"])
            else:
                return {
                    "is_successful_execution": False,
                    "msg": 'User Id exists'
                }
            return sign_up_query_response

        except Exception as err:
            return flask_request_response.error_response(
                str(err), SIGN_UP_API, POST_REQUEST
            )
