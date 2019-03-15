"""Initialize database."""

from . import db_nomenclature
from .connection import CONNECTION


def db_init():
    """Create databse and collections for first time."""
    CONNECTION.createDatabase(name=db_nomenclature.DATABASE)
    _db = CONNECTION[db_nomenclature.DATABASE]
    _db.createCollection(name=db_nomenclature.USER_COLLECTION)
    _db.createCollection(name=db_nomenclature.THEME_COLLECTION)
    _db.createCollection(name=db_nomenclature.TOPIC_COLLECTION)
    _db.createCollection(name=db_nomenclature.ASSESSMENT_COLLECTION)
    _db.createCollection(name=db_nomenclature.QUESTION_COLLECTION)
    _db.createCollection(name=db_nomenclature.RESOURCE_COLLECTION)


if __name__ == "__main__":
    db_init()
