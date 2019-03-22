from content_creation_db.db import db_nomenclature, db_objects


def update_question_query(question_data):
    """Query to create a question.

    Parameters
    ----------
    question_data : object

    """
    return """
        REPLACE "{key}" WITH {question} IN {question_collection}
        RETURN {{"is_successfult_execution": true}}
        """.format(
            key=question_data["_key"],
            question=question_data,
            question_collection=db_nomenclature.QUESTION_COLLECTION
        )


def update_question_query_response(question_data):
    query_response = db_objects.graph_db().AQLQuery(
        update_question_query(question_data)
    ).response
    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}

    data = query_response['result'][0]
    return data
