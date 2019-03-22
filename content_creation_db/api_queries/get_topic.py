from content_creation_db.db import db_nomenclature, db_objects


def get_topic_query(topic_id):
    """Query to create a topic.

    Parameters
    ----------
    topic_id : string

    """
    return """
        LET topic = (
            RETURN DOCUMENT("{topic_collection}", "{topic_id}")
        )
        RETURN {{"is_successfult_execution": true, topic: topic[0]}}
        """.format(
            topic_id=topic_id,
            topic_collection=db_nomenclature.TOPIC_COLLECTION
        )


def get_topic_query_response(topic_id):
    query_response = db_objects.graph_db().AQLQuery(
        get_topic_query(topic_id)
    ).response
    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}

    data = query_response['result'][0]
    return data
