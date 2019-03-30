from content_creation_db.db import db_nomenclature, db_objects


def signup_query(signup_details):
    """Query to sign up a new user.

    sign up new user only if the user id is unique

    Parameters
    ----------
    signup_details : [type]
        [description]

    """
    return """
    INSERT {signup_details} IN {user_collection}
    RETURN {{
        "is_successful_execution": true
    }}
    """.format(
        signup_details=signup_details,
        user_collection=db_nomenclature.USER_COLLECTION
    )


def signup_query_response(signup_details):
    query_response = db_objects.graph_db().AQLQuery(
        signup_query(signup_details)
    ).response
    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}

    return query_response['result'][0]
