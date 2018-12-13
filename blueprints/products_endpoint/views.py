# -*- coding: utf-8 -*-

# ThirdParty Library
import imghdr
# Standard Library
from logging import getLogger

from flask import current_app as app
from flask import request
from flask_restful import Resource
from webargs import fields
from webargs.flaskparser import use_args
from werkzeug.exceptions import BadRequest

from .helpers import get_tags

logger = getLogger(__name__)


class GetProducts(Resource):
    def post(self):
        result = []
        available_types = app.config["AVAILABLE_IMAGE_TYPES"]
        if 'file' not in request.files:
            raise BadRequest("Invalid multiple key for files")
        for image in request.files.getlist("file"):
            if not bool(image.filename) or imghdr.what(
                    image) not in available_types:
                continue
            image_bytes = image.read()
            tags = get_tags(image_bytes)
            part_result = {'tags': tags}
            # TODO: add api call for some service
            result.append(part_result)
        return result


# example with args
# class GetProducts(Resource):
#     args = {
#         "type":
#         fields.Str(required=True, validate=lambda x: x in Config.SOME_LIST)
#     }
#
#     @use_args(args, locations=("query",))
#     def post(self, args):
#       *method_body*