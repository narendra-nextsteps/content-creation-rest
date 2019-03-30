from content_creation_db.db import db_nomenclature, db_objects


def login_query(user_id, password):
    """Query to check login details validity.

    Parameters
    ----------
    login_details : dict

    """
    return """
    LET user = (
    FOR user in {users_collection}
        FILTER user.user_id == "{user_id}"
        FILTER user.password == "{password}"
        RETURN user
    )

    RETURN user[0] ? {{user_id: user[0]["user_id"], name: user[0]["name"], \
        role: user[0]["role"], is_successful_execution: true}} : \
        {{msg: "wrong details", is_successful_execution: false}}
    """.format(
        user_id=user_id,
        password=password,
        users_collection=db_nomenclature.USER_COLLECTION
    )


def login_query_response(user_id, password):
    """Get the login query response.

    Parameters
    ----------
    login_details : dict

    """
    query_response = db_objects.graph_db().AQLQuery(
        login_query(user_id, password)
    ).response

    print(query_response)

    if query_response['error'] or not query_response['result']:
        return {
            "is_successful_execution": False
        }
    return query_response['result'][0]
