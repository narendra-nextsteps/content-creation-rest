from content_creation_db.db import db_nomenclature, db_objects


def create_assessment_query(assessment_data):
    """Query to create a assessment.

    Parameters
    ----------
    assessment_data : object

    """
    return """
        LET assessment = {assessment}
        INSERT assessment IN {assessments_collection}
        RETURN {{
            "is_successfull_execution": true, assessment_id: assessment.id
        }}
        """.format(
        assessment=assessment_data,
        assessments_collection=db_nomenclature.ASSESSMENT_COLLECTION
    )


def create_assessment_query_response(assessment_data):
    query_response = db_objects.graph_db().AQLQuery(
        create_assessment_query(assessment_data)
    ).response
    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}

    data = query_response['result'][0]
    return data
