from content_creation_db.db import db_nomenclature, db_objects


def create_theme_query(theme_data):
    """Query to create a theme.

    Parameters
    ----------
    theme_data : object

    """
    return """
        INSERT {theme} IN {theme_collection}
        RETURN {{"is_successfult_execution": true}}
        """.format(
            theme=theme_data,
            theme_collection=db_nomenclature.THEME_COLLECTION
        )


def create_theme_query_response(theme_data):
    query_response = db_objects.graph_db().AQLQuery(
        create_theme_query(theme_data)
    ).response
    if query_response['error'] or not query_response['result']:
        return {"is successful execution": False}

    data = query_response['result'][0]
    return data
