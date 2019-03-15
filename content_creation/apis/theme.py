from flask_restful import Resource
from content_creation import flask_request_response
from content_creation_db.protos import request_pb2
from content_creation_db.api_queries.create_theme import \
    create_theme_query_response
from content_creation_db.api_queries.update_theme import \
    update_theme_query_reponse
from google.protobuf import json_format

POST_REQUEST = 'POST'
PUT_REQUEST = "PUT"
THEME_API = '/theme'


class Theme(Resource):
    """CRUD operations on questions."""

    def post(self):
        """Create new theme."""
        msg_request, err_msg = flask_request_response.message_request(
            request_pb2.CreateThemeRequest, THEME_API, POST_REQUEST
        )
        if err_msg is not None:
            return flask_request_response.error_response(
                err_msg["err_message"], THEME_API, POST_REQUEST
            )
        try:
            json_request = json_format.MessageToDict(
                msg_request, preserving_proto_field_name=True)
            query_response = create_theme_query_response(
                json_request['theme'])
            return query_response
        except Exception as err:
            return flask_request_response.error_response(
                str(err), THEME_API, POST_REQUEST
            )

    def put(self):
        "Update theme."""
        msg_request, err_msg = flask_request_response.message_request(
            request_pb2.CreateThemeRequest, THEME_API, PUT_REQUEST
        )
        if err_msg is not None:
            return flask_request_response.error_response(
                err_msg["err_message"], THEME_API, PUT_REQUEST
            )
        try:
            json_request = json_format.MessageToDict(
                msg_request, preserving_proto_field_name=True)
            query_response = update_theme_query_reponse(
                json_request['theme'])
            return query_response
        except Exception as err:
            return flask_request_response.error_response(
                str(err), THEME_API, PUT_REQUEST
            )
