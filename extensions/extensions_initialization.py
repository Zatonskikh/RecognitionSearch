# -*- coding: utf-8 -*-
from flask_cors import CORS
from flask_wtf import CSRFProtect

from .flask_dd_client import FlaskDeepDetect

csrf_protect = CSRFProtect()
cors = CORS()
deep_detect_extension = FlaskDeepDetect()
