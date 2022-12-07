from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from schema import PlainProductSchema
from models import ProductsModel
from db import db

blp = Blueprint("Products", "products", description="Operations on products")


@blp.route("/products/<string:orders>")
class Products(MethodView):

    @blp.response(200, PlainProductSchema)
    def get(self, orders):
        products = ProductsModel.query.get_or_404(orders)
        return products

