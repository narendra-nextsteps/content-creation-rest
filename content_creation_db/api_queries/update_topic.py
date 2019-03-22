from content_creation_db.db import db_nomenclature, db_objects


def update_topic_query(topic_data):
    """Query to create a topic.

    Parameters
    ----------
    topic_data : object

    """
    return """
        REPLACE "{key}" WITH {topic} IN {topic_collection}
        RETURN {{"is_successfult_execution": true}}
        """.format(
            key=topic_data["_key"],
            topic=topic_data,
            topic_collection=db_nomenclature.TOPIC_COLLECTION
        )


def update_topic_query_response(topic_data):
    query_response = db_objects.graph_db().AQLQuery(
        update_topic_query(topic_data)
    ).response
    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}

    data = query_response['result'][0]
    return data
