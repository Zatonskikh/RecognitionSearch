# -*- coding: utf-8 -*-

from flask.helpers import get_debug_flag

from app import create_app
from settings import Config

app = create_app(Config)

if __name__ == "__main__":
    app.run()