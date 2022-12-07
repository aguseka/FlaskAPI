from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import ShippingMethodsModel
from schema import PlainShippingSchema

blp = Blueprint("Shipping", "shipping", description="Operations on shipping")


@blp.route("/shipping/<string:shipping_id>")
class Customer(MethodView):
    @blp.response(200, PlainShippingSchema)
    def get(self, shipping_id):
        shipping = ShippingMethodsModel.query.get_or_404(shipping_id)
        return shipping

