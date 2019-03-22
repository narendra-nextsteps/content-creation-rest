from content_creation_db.db import db_nomenclature, db_objects


def create_topic_query(topic_data):
    """Query to create a topic.

    Parameters
    ----------
    topic_data : object

    """
    return """
        LET topic = {topic}
        INSERT topic IN {topics_collection}
        RETURN {{
            "is_successfull_execution": true, topic_id: topic.id
        }}
        """.format(
        topic=topic_data,
        topics_collection=db_nomenclature.TOPIC_COLLECTION
    )


def create_topic_query_response(topic_data):
    print("==============================")
    print(topic_data)
    print("==============================")
    query_response = db_objects.graph_db().AQLQuery(
        create_topic_query(topic_data)
    ).response
    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}

    data = query_response['result'][0]
    return data
