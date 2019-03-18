from content_creation_db.db import db_nomenclature, db_objects


def get_assessment_query(assessment_id):
    """Query to create a assessment.

    Parameters
    ----------
    assessment_id : string

    """
    return """
        LET assessment = (
            RETURN DOCUMENT("{assessment_collection}", "{assessment_id}")
        )
        RETURN {{"is_successfult_execution": true, assessment: assessment[0]}}
        """.format(
            assessment_id=assessment_id,
            assessment_collection=db_nomenclature.ASSESSMENT_COLLECTION
        )


def get_assessment_query_response(assessment_id):
    query_response = db_objects.graph_db().AQLQuery(
        get_assessment_query(assessment_id)
    ).response
    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}

    data = query_response['result'][0]
    return data
