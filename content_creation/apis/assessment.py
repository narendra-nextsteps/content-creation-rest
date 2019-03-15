from flask_restful import Resource
from content_creation import flask_request_response
from content_creation_db.protos import request_pb2
from content_creation_db.api_queries.create_assessment import \
    create_assessment_query_response
from google.protobuf import json_format

POST_REQUEST = 'POST'
ASSESSMENT_API = '/assessment'


class Assessment(Resource):
    """CRUD operations on questions."""

    def post(self):
        """Create new assessment."""
        msg_request, err_msg = flask_request_response.message_request(
            request_pb2.CreateAssessmentRequest, ASSESSMENT_API, POST_REQUEST
        )
        if err_msg is not None:
            return flask_request_response.error_response(
                err_msg["err_message"], ASSESSMENT_API, POST_REQUEST
            )
        try:
            json_request = json_format.MessageToDict(
                msg_request, preserving_proto_field_name=True)
            query_response = create_assessment_query_response(
                json_request['assessment'])
            return query_response
        except Exception as err:
            return flask_request_response.error_response(
                str(err), ASSESSMENT_API, POST_REQUEST
            )
