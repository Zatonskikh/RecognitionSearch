from flask import Blueprint
from flask_restful import Api

from .views import GetProducts

blueprint = Blueprint('products_endpoint', __name__)

api = Api(blueprint)

api.add_resource(GetProducts, '/suggest_products')
