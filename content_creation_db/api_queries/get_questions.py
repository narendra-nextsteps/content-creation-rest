from content_creation_db.db import db_nomenclature, db_objects


def get_questions_query(question_ids):
    """Query to create a question.

    Parameters
    ----------
    question_ids : list

    """
    return """
        LET questions = (
            FOR id IN {question_ids}
            RETURN DOCUMENT("{question_collection}", id)
        )
        RETURN {{"is_successfult_execution": true, questions: questions}}
        """.format(
            question_ids=question_ids,
            question_collection=db_nomenclature.QUESTION_COLLECTION
        )


def get_questions_query_response(question_ids):
    query_response = db_objects.graph_db().AQLQuery(
        get_questions_query(question_ids)
    ).response
    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}

    data = query_response['result'][0]
    return data
