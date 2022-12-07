from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import CustomersModel
from schema import PlainCustomerSchema

blp = Blueprint("Customers", "customers", description="Operations on customers")


@blp.route("/customer/<string:customer_id>")
class Customer(MethodView):
    @blp.response(200, PlainCustomerSchema)
    def get(self, customer_id):
        customer = CustomersModel.query.get_or_404(customer_id)
        return customer
