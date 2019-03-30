from content_creation_db.db import db_nomenclature, db_objects


def get_assessment_details_query(assessment_ids):
    """Query to create a question.

    Parameters
    ----------
    assessment_ids : list

    """
    return """
    LET assessment_details = (
        FOR id IN {assessment_ids}
        RETURN DOCUMENT("{assessment_collection}", id)
    )
    RETURN {{"is_successfult_execution": true,
        assessment_details: assessment_details}}
    """.format(
        assessment_ids=assessment_ids,
        assessment_collection=db_nomenclature.ASSESSMENT_COLLECTION
    )


def get_assessment_details_query_response(assessment_ids):
    query_response = db_objects.graph_db().AQLQuery(
        get_assessment_details_query(assessment_ids)
    ).response
    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}
    print(query_response)
    data = query_response['result'][0]
    return data
