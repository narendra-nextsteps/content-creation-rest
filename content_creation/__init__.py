import os
from flask import Flask
from flask_cors import CORS

# pylint: disable=c0103, c0413

app = Flask(__name__)
CORS(app)
app.config.from_object("content_creation.default_settings")
app.config.from_envvar('CONTENT_CREATION_SETTINGS')

if not app.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler
    # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
    file_handler = TimedRotatingFileHandler(
        os.path.join(app.config['LOG_DIR'], 'content_creation.log'), 'midnight'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        '<%(asctime)s> <%(levelname)s> %(message)s'
    ))
    app.logger.addHandler(file_handler)

import content_creation.apis  # noqa
