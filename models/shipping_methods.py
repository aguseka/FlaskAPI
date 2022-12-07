#models/shipping_modethods.py
from db import db
class ShippingMethodsModel(db.Model):
    __tablename__ = "shipping_methods"
    shipping_method_id = db.Column(db.Integer,primary_key = True) 
    shipping_method = db.Column(db.String(20),unique = True, nullable = False)
    order = db.relationship("OrdersModel", back_populates = "shipping", lazy = "dynamic")

