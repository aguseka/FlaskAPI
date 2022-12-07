#models/employees.py
from db import db
class EmployeesModel(db.Model):
    __tablename__ = "employees"
    employee_id = db.Column(db.Integer,primary_key = True) 
    first_name = db.Column(db.String(50),unique = False, nullable = False)
    last_name = db.Column(db.String(50),unique = False, nullable = False)
    title = db.Column(db.String(50),unique = False, nullable = False)
    work_phone = db.Column(db.String(30),unique = True, nullable = False)
    order = db.relationship("OrdersModel", back_populates = "employee", lazy = "dynamic")
    
    def __init__(
        employee_id:int,
        first_name:str,
        last_name:str, 
        title:str, 
        work_phone:str,
        ):
        
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name 
        self.title,  = title
        self.work_phone = work_phone

    
    @staticmethod
    def create(
        employee_id, 
        first_name, 
        last_name, 
        title, 
        work_phone,
        ):
        
        new_employee = (
        employee_id, 
        first_name, 
        last_name, 
        title, 
        work_phone,
        )
        
        db.session.add(new_employee)
        db.session.commit()
        
