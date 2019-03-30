from content_creation_db.db import db_nomenclature, db_objects


def get_topic_details_query(topic_ids):
    """Query to create a question.

    Parameters
    ----------
    topic_ids : list

    """
    return """
    LET topic_details = (
        FOR id IN {topic_ids}
        RETURN DOCUMENT("{topic_collection}", id)
    )
    RETURN {{"is_successfult_execution": true,
        topic_details: topic_details}}
    """.format(
        topic_ids=topic_ids,
        topic_collection=db_nomenclature.TOPIC_COLLECTION
    )


def get_topic_details_query_response(topic_ids):
    query_response = db_objects.graph_db().AQLQuery(
        get_topic_details_query(topic_ids)
    ).response
    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}
    print(query_response)
    data = query_response['result'][0]
    return data
