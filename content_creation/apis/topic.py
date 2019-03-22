from flask_restful import Resource
from google.protobuf import json_format
from content_creation import flask_request_response
from content_creation_db.protos import request_pb2
from content_creation_db.api_queries.create_topic import \
    create_topic_query_response
from content_creation_db.api_queries.get_topic import \
    get_topic_query_response
from content_creation_db.api_queries.update_topic import \
    update_topic_query_response

POST_REQUEST = 'POST'
PUT_REQUEST = "PUT"
TOPIC_API = '/topic/<string:topic_id>'


class Topic(Resource):
    """CRUD operations on questions."""

    def get(self, topic_id):
        query_response = get_topic_query_response(topic_id)
        return query_response

    def post(self, topic_id):
        """Create new topic."""
        msg_request, err_msg = flask_request_response.message_request(
            request_pb2.CreateTopicRequest, TOPIC_API, POST_REQUEST
        )
        if err_msg is not None:
            return flask_request_response.error_response(
                err_msg["err_message"], TOPIC_API, POST_REQUEST
            )
        try:
            json_request = json_format.MessageToDict(
                msg_request, preserving_proto_field_name=True)
            query_response = create_topic_query_response(
                json_request['topic'])
            return query_response
        except Exception as err:
            return flask_request_response.error_response(
                str(err), TOPIC_API, POST_REQUEST
            )

    def put(self, topic_id):
        """Create new topic."""
        msg_request, err_msg = flask_request_response.message_request(
            request_pb2.CreateTopicRequest, TOPIC_API, PUT_REQUEST
        )
        if err_msg is not None:
            return flask_request_response.error_response(
                err_msg["err_message"], TOPIC_API, PUT_REQUEST
            )
        try:
            json_request = json_format.MessageToDict(
                msg_request, preserving_proto_field_name=True)
            query_response = update_topic_query_response(
                json_request['topic'])
            return query_response
        except Exception as err:
            return flask_request_response.error_response(
                str(err), TOPIC_API, PUT_REQUEST
            )

