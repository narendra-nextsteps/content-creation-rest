from content_creation_db.db import db_nomenclature, db_objects


def get_theme_query(theme_id):
    """Query to create a theme.

    Parameters
    ----------
    theme_id : object

    """
    return """
        LET theme = (
            RETURN DOCUMENT("{theme_collection}", "{theme_id}")
        )
        LET assessmentsDetails = (
            FILTER theme[0].assessment_ids
            FOR assessmentId in theme[0].assessment_ids
                FOR assessment in Assessments
                    FILTER assessment.id == assessmentId
                return assessment
        )

        LET topicDetails = (
            FILTER theme[0].topic_ids
            FOR topicId in theme[0].topic_ids
                FOR topic in Topics
                    FILTER topic.id == topicId
                return topic
        )
        RETURN {{"is_successfult_execution": true, theme: theme[0],
            assessmentsDetails: assessmentsDetails, topicDetails: topicDetails}}
        """.format(
        theme_id=theme_id,
        theme_collection=db_nomenclature.THEME_COLLECTION
    )


def get_theme_query_response(theme_id):
    query_response = db_objects.graph_db().AQLQuery(
        get_theme_query(theme_id)
    ).response
    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}

    data = query_response['result'][0]
    return data
