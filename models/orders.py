#models/orders.py
from db import db


class OrdersModel(db.Model):

    __tablename__ = "orders"

    orders_id = db.Column(db.Integer,primary_key = True) 
    customer_id = db.Column(db.Integer,db.ForeignKey("customers.customer_id"), unique = False, nullable = False)#check again
    customer = db.relationship("CustomersModel", back_populates="order")
    employee_id = db.Column(db.Integer,db.ForeignKey("employees.employee_id"), unique = False, nullable = False)
    employee = db.relationship("EmployeesModel", back_populates="order")
    order_date = db.Column(db.Date)
    purchase_order_number = db.Column(db.String(30), unique = True, nullable = False)
    ship_date = db.Column(db.Date)
    shipping_method_id = db.Column(db.Integer, db.ForeignKey("shipping_methods.shipping_method_id"), unique = False, nullable = False)
    shipping = db.relationship("ShippingMethodsModel", back_populates="order")
    freight_charge = db.Column(db.Integer, unique = False, nullable = False)
    taxes = db.Column(db.Integer, unique = False, nullable = False)
    payment_received = db.Column(db.CHAR(1), unique = False, nullable = False)
    comment  = db.Column(db.String(150), unique = False, nullable = False)
    order_details = db.relationship("OrderDetailsModel", back_populates = "order", lazy = "dynamic" )
    
    
    def __init__():
        pass
    
    @staticmethod
    def create():
        pass