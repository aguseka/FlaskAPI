#models/order_details.py
from db import db
class OrderDetailsModel(db.Model):
    __table__name = "order_details"
   
    order_detail_id = db.Column(db.Integer,primary_key = True) 
    orders_id = db.Column(db.Integer,db.ForeignKey("orders.orders_id"), unique=False, nullable = False)
    order = db.relationship("OrdersModel", back_populates = "order_details")
    product_id = db.Column(db.Integer,db.ForeignKey("products.products_id"), unique = False, nullable = False)
    products = db.relationship("ProductsModel", back_populates = "order_details")
    quantity = db.Column(db.Integer, unique = False, nullable = False)
    unit_price = db.Column(db.Float(precision = 2))
    discount = db.Column(db.Float(precision = 2))
    

    def __init__():
        pass
    
    @staticmethod
    def create():
        pass