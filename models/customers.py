# models/customers.py
from db import db


class CustomersModel(db.Model):
    __tablename__ = "customers"
    customer_id = db.Column(db.Integer, primary_key = True) 
    company_name = db.Column(db.String(50),unique = False, nullable = False)
    first_name = db.Column(db.String(30),unique = False, nullable = False)
    last_name = db.Column(db.String(50),unique = False, nullable = False)
    billing_address = db.Column(db.String(255),unique = False, nullable = False)
    city = db.Column(db.String(50),unique = False, nullable = False)
    state_or_province = db.Column(db.String(20),unique = False, nullable = False)
    zip_code = db.Column(db.String(20),unique = False, nullable = False)
    email = db.Column(db.String(75),unique = True, nullable = False)
    company_website = db.Column(db.String(200),unique = False, nullable = True)
    phone_number = db.Column(db.String(30),unique = False, nullable = False)
    fax_number = db.Column(db.String(30),unique = False, nullable = True)
    ship_address = db.Column(db.String(255),unique = False, nullable = False)
    ship_city = db.Column(db.String(50),unique = False, nullable = False)
    ship_state_or_province = db.Column(db.String(250),unique = False, nullable = False)
    ship_zip_code = db.Column(db.String(20), unique = False, nullable = False)
    ship_phone_number = db.Column(db.String(30), unique = True, nullable = False)
    order = db.relationship("OrdersModel", back_populates = "customer", lazy = "dynamic")
    
    def __init__(self, 
            customer_id: int,
            company_name: str, 
            first_name:str, 
            last_name :str,
            billing_address:str, 
            city:str, 
            state_or_province:str, 
            zip_code:str, 
            email:str, 
            company_website:str, 
            phone_number:str, 
            fax_number:str, 
            ship_address:str, 
            ship_city :str,
            ship_state_or_province:str,
            ship_zip_code:str, 
            ship_phone_number:str,
        ):
            self.customer_id = customer_id
            self.company_name = company_name
            self.first_name = first_name
            self.last_name = last_name
            self.billing_address = billing_address
            self.city = city 
            self.state_or_province = state_or_province
            self.zip_code = zip_code
            self.email = email 
            self.company_website = company_website
            self.phone_number = phone_number
            self.fax_number = fax_number
            self.ship_address = ship_address
            self.ship_city = ship_city
            self.ship_state_or_province = ship_state_or_province 
            self.ship_zip_code = ship_zip_code 
            self.ship_phone_number = ship_phone_number
                
    @staticmethod
    def create(customer_id, 
                company_name, 
                first_name, 
                last_name, 
                billing_address, 
                city, 
                state_or_province, 
                zip_code, 
                email, 
                company_website, 
                phone_number, 
                fax_number, 
                ship_address, 
                ship_city, 
                ship_state_or_province, 
                ship_zip_code, 
                ship_phone_number,):  
                
            new_user = CustomersModel( # create new user
                customer_id, 
                company_name, 
                first_name, 
                last_name, 
                billing_address, 
                city, 
                state_or_province, 
                zip_code, 
                email, 
                company_website, 
                phone_number, 
                fax_number, 
                ship_address, 
                ship_city, 
                ship_state_or_province, 
                ship_zip_code, 
                ship_phone_number, 
            )
            db.session.add(new_user)
            db.session.commit()
    
    