"""Create Connection to database."""
from pyArango.connection import Connection

from . import settings

CONNECTION = Connection(username=settings.USERNAME, password=settings.PASSWORD,
                        arangoURL=settings.CONNECTION_URLS)
