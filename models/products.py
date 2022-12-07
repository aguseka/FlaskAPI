# models/products.py
from db import db


class ProductsModel(db.Model):
    __tablename__ = "products"
    products_id = db.Column(db.Integer, unique=True, primary_key=True)
    product_name = db.Column(db.String(50), unique=True, nullable=False)
    unit_price = db.Column(db.Float(precision=2), nullable=False)
    order_details = db.relationship("OrderDetailsModel", back_populates = "products", lazy = "dynamic")



    def __init__( 
        product_id:int, 
        product_name:str,
        unit_price:float, ):
        
        self.product_id = product_id
        self.product_name = product_name
        self.unit_price = product_price
    
    @staticmethod
    def create(
        product_id, 
        product_name, 
        unit_price,
        ):
        new_product = ProductsModel(
            product_id,
            product_name, 
            unit_price,
        )
        db.session.add(new_product)
        db.session.commit()
