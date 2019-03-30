from content_creation_db.db import db_nomenclature, db_objects


def check_user_id_exists_query(user_id):
    """Query to check user id exits or not.

    Parameters
    ----------
    user_id : string

    """
    return """
    RETURN !IS_NULL(DOCUMENT({users_collection}, "{user_id}"))
    """.format(
        user_id=user_id,
        users_collection=db_nomenclature.USER_COLLECTION
    )


def check_user_id_exists_query_response(user_id):
    """Query for user id exists or not and respond accordingly.

    Parameters
    ----------
    user_id : string

    """
    query_response = db_objects.graph_db().AQLQuery(
        check_user_id_exists_query(user_id)
    ).response
    print("-==========", check_user_id_exists_query(user_id), query_response)

    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}

    return query_response['result'][0]
