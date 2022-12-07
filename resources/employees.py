from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from schema import PlainEmployeeSchema
from models import EmployeesModel
blp = Blueprint("Employees", "employees", description="Operations on employees")


@blp.route("/employee/<string:employee_id>")
class Employee(MethodView):
    @blp.response(200, PlainEmployeeSchema)
    def get(self, item_id):
        employee = EmployeesModel.query.get_or_404(employee_id)
        return employee
