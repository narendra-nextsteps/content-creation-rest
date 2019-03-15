from flask_restful import Resource
from content_creation import flask_request_response
from content_creation_db.protos import request_pb2
from content_creation_db.api_queries.my_content import \
    get_my_contents_query_response
from google.protobuf import json_format

POST_REQUEST = 'POST'
MY_CONTENT_API = '/my-content'


class MyContent(Resource):
    """Get Content created by user."""

    def post(self):
        """Create new assessment."""
        msg_request, err_msg = flask_request_response.message_request(
            request_pb2.UserContentRequest, MY_CONTENT_API, POST_REQUEST
        )
        if err_msg is not None:
            return flask_request_response.error_response(
                err_msg["err_message"], MY_CONTENT_API, POST_REQUEST
            )
        try:
            json_request = json_format.MessageToDict(
                msg_request, preserving_proto_field_name=True)
            query_response = get_my_contents_query_response(
                json_request['user_id'])
            return query_response
        except Exception as err:
            return flask_request_response.error_response(
                str(err), MY_CONTENT_API, POST_REQUEST
            )
