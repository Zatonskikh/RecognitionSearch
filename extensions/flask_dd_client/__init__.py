# -*- coding: utf-8 -*-
from flask import Flask
from .dd_client import DD


class FlaskDeepDetect(object):
    """Work with deepdetect."""

    def __init__(self, app: Flask = None):
        """Create instanse class."""

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialization of deep detect api."""

        host = app.config.get('RECOGNITION_SERVICE_HOST')
        port = app.config.get('RECOGNITION_SERVICE_PORT')
        scheme = app.config.get('RECOGNITION_SERVICE_SCHEME')

        # deep detect client - proto == 0 -> http, else https
        proto = 0
        if scheme == 'https':
            proto = 1
        dd = DD(host, port=port, proto=proto)
        dd.set_return_format(dd.RETURN_PYTHON)
        app.deep_detect = dd
