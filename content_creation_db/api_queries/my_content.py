from content_creation_db.db import db_nomenclature, db_objects


def get_my_contents_query(user_id):
    """Query to create a assessment.

    Parameters
    ----------
    user_id : string

    """
    return """
        LET user_id = "{user_id}"

        LET themes = (
            FOR theme IN {themes_collection}
                FILTER theme.created_by == user_id
            RETURN theme
        )

        LET assessments = (
            FOR assessment IN {assessments_collection}
                FILTER assessment.created_by == user_id AND assessment.themes \
                    == NULL
            RETURN assessment
        )

        LET topics = (
            FOR topic IN {topic_collection}
                FILTER topic.created_by == user_id AND topic.themes == NULL
            RETURN topic
        )

        RETURN {{
            themes: themes,
            topics: topics,
            assessments: assessments
        }}

        """.format(
        user_id=user_id,
        assessments_collection=db_nomenclature.ASSESSMENT_COLLECTION,
        themes_collection=db_nomenclature.THEME_COLLECTION,
        topic_collection=db_nomenclature.TOPIC_COLLECTION
    )


def get_my_contents_query_response(user_id):
    query_response = db_objects.graph_db().AQLQuery(
        get_my_contents_query(user_id)
    ).response
    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}

    data = query_response['result'][0]
    return data
