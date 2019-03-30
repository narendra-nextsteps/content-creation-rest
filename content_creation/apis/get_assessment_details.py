from flask_restful import Resource
from content_creation import flask_request_response
from content_creation_db.protos import request_pb2
from content_creation_db.api_queries.get_assessment_details import \
    get_assessment_details_query_response
from google.protobuf import json_format

POST_REQUEST = 'POST'
GET_ASSESSMENT_DETAILS_API = '/get-assessment-details'


class GetAssessments(Resource):
    """CRUD operations on questions."""

    def post(self):
        """Create new question."""
        msg_request, err_msg = flask_request_response.message_request(
            request_pb2.GetAssessments, GET_ASSESSMENT_DETAILS_API, POST_REQUEST
        )
        if err_msg is not None:
            return flask_request_response.error_response(
                err_msg["err_message"],
                GET_ASSESSMENT_DETAILS_API,
                POST_REQUEST
            )
        try:
            json_request = json_format.MessageToDict(
                msg_request, preserving_proto_field_name=True)
            query_response = get_assessment_details_query_response(
                json_request['ids'])
            return query_response
        except Exception as err:
            return flask_request_response.error_response(
                str(err), GET_ASSESSMENT_DETAILS_API, POST_REQUEST
            )
