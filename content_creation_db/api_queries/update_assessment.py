from content_creation_db.db import db_nomenclature, db_objects


def update_assessment_query(assessment_data):
    """Query to create a assessment.

    Parameters
    ----------
    assessment_data : object

    """
    return """
        REPLACE "{key}" WITH {assessment} IN {assessment_collection}
        RETURN {{"is_successfult_execution": true}}
        """.format(
            key=assessment_data["_key"],
            assessment=assessment_data,
            assessment_collection=db_nomenclature.ASSESSMENT_COLLECTION
        )


def update_assessment_query_response(assessment_data):
    query_response = db_objects.graph_db().AQLQuery(
        update_assessment_query(assessment_data)
    ).response
    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}

    data = query_response['result'][0]
    return data
