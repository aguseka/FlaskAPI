from faker import Faker
from faker.providers import DynamicProvider
from app import create_app
from random import randint
from models.customers import CustomersModel
from models.employees import EmployeesModel
from models.products import ProductsModel
from models.orders import OrdersModel
from models.order_details import OrderDetailsModel

from models.customers import CustomersModel


def insert_dummy_data():
    app = create_app()
    fake = Faker()
    zip_code_provider = DynamicProvider(
         provider_name="zip_code",
         elements=["81151", "12000", "82245", "11000", "17000"]
    )
    state_provider = DynamicProvider(
         provider_name="state",
         elements=["DKI Jakarta", "Bali", "Jawa Timur", "Jawa Tengah", "Jawa Barat", "Banten", "Sumatra Barat", "Sumatra Selatan"
         "Sumatra Utara", "Aceh", "Kalimantan Utara", "Kalimantan Selatan", "Kalimantan Timur", "Kalimantan Barat", "Sulewesi Selatan",
         "Sulawesi Tenggara", " Maluku", "Papua", "NTB", "NTT" ])
    
    
    product_provider = DynamicProvider(
        provider_name = "product",
        elements =["Samsung", "Smartwatch", "LED TV", "Toy Laptop", "Dog Toys ","Ball","SmartTV","Nasi Bungkus","Kerupuk Udang", "T-shirt"]
    )
    shipping_provider = DynamicProvider(
        provider_name = "shipping",
        elements =["DHL Land"," JNE", "Si Cepat", "Satria", "Fedex"]
    )
    
    website_provider = DynamicProvider(
        provider_name = "website",
        elements =["kompas.com", "detik.com", "telkom.co.id","kontan.co.id", "indomiliter.com", "jejaktapak.com", "nytimes.com", "sciencedaily.com"]
    )
    
    fake.add_provider(zip_code_provider)
    fake.add_provider(state_provider)
    fake.add_provider(product_provider)
    fake.add_provider(shipping_provider)
    fake.add_provider(website_provider)
    
    
    for cus in range(10):
         with app.app_context():
             CustomersModel.create(
                 cus+1,#customer_id = db.Column(db.Integer, primary_key = True) 
                 fake.company(),#company_name = db.Column(db.String(50),unique = False, nullable = False)
                 fake.first_name(),#first_name = db.Column(db.String(30),unique = False, nullable = False)
                 fake.last_name(),#last_name = db.Column(db.String(50),unique = False, nullable = False)
                 fake.address(),#billing_address = db.Column(db.String(255),unique = False, nullable = False)
                 fake.city(),#city = db.Column(db.String(50),unique = False, nullable = False)
                 fake.state(),#state_or_province = db.Column(db.String(20),unique = False, nullable = False)
                 fake.zip_code(),#zip_code = db.Column(db.String(20),unique = False, nullable = False)
                 fake.email(),#email = db.Column(db.String(75),unique = True, nullable = False)
                 fake.website(),#company_website = db.Column(db.String(200),unique = False, nullable = True)
                 fake.phone_number(),#phone_number = db.Column(db.String(30),unique = False, nullable = False)
                 fake.phone_number(),#fax_number = db.Column(db.String(30),unique = False, nullable = True)
                 fake.address(),#ship_address = db.Column(db.String(255),unique = False, nullable = False)
                 fake.city(),#ship_city = db.Column(db.String(50),unique = False, nullable = False)
                 fake.state(),#ship_state_or_province = db.Column(db.String(250),unique = False, nullable = False)
                 fake.zip_code(),#ship_zip_code = db.Column(db.String(20), unique = False, nullable = False)
                 fake.phone_number(),#ship_phone_number = db.Column(db.String(30), unique = True, nullable = False)
                 #order = db.relationship("OrdersModel", back_populates = "customer ", lazy = "dynamic")
                 )
    
    for emp in range(10):
         with app.app_context():
             EmployeesModel.create(
                 emp+1,#employee_id = db.Column(db.Integer,primary_key = True) 
                 fake.first_name(),#first_name = db.Column(db.String(50),unique = False, nullable = False)
                 fake.last_name(),#last_name = db.Column(db.String(50),unique = False, nullable = False)
                 'operator',#title = db.Column(db.String(50),unique = False, nullable = False)
                 '12345678',#work_phone = db.Column(db.String(30),unique = True, nullable = False)
             )
    for pro in range(25):
         with app.app_context():
             ProductsModel.create(
                 prod+1,#products_id = db.Column(db.Integer, unique=True, primary_key=True)
                 fake.product(),#product_name = db.Column(db.String(50), unique=True, nullable=False)
                 random.randint(25,50),#unit_price = db.Column(db.Float(precision=2), nullable=False)
                 #order_details = db.relationship("OrderDetailsModel", back_populates = "products", lazy = "dynamic")
                )
                
    for shp in range(5):
         with app.app_context():
             ShippingMethodsModel.create(
                 shp+1,#shipping_method_id = db.Column(db.Integer,primary_key = True) 
                 fake.shipping(),#shipping_method = db.Column(db.String(20),unique = True, nullable = False)
                 #order = db.relationship("OrdersModel", back_populates = "shipping", lazy = "dynamic")   
             )           
                
                
    for ord in range(50):
         with app.app_context():
             OrdersModel.create(
                 ord+1,#orders_id = db.Column(db.Integer,primary_key = True) 
                 random.randint(1,10),#customer_id = db.Column(db.Integer,db.ForeignKey("customers.customer_id"), unique = False, nullable = False)#check again
                 #customer = db.relationship("CustomersModel", back_populates="order")
                 random.randint(1,10),#employee_id = db.Column(db.Integer,db.ForeignKey("employees.employee_id"), unique = False, nullable = False)
                 #employee = db.relationship("EmployeesModel", back_populates="order")
                 fake.date(),#order_date = db.Column(db.Date)
                 #purchase_order_number = db.Column(db.String(30), unique = True, nullable = False)
                 #ship_date = db.Column(db.Date)
                 random.randint(1,5),#shipping_method_id = db.Column(db.Integer, db.ForeignKey("shipping_methods.shipping_method_id"), unique = False, nullable = False)
                 #shipping = db.relationship("ShippingMethodsModel", back_populates="order")
                 random.randint(1,5),#freight_charge = db.Column(db.Integer, unique = False, nullable = False)
                 #taxes = db.Column(db.Integer, unique = False, nullable = False)
                 random.randint(0,1),#payment_received = db.Column(db.CHAR(1), unique = False, nullable = False)
                 fake.sentence(),#comment  = db.Column(db.String(150), unique = False, nullable = False)
                 #order_details = db.relationship("OrderDetailsModel", back_populates = "order", lazy = "dynamic" )
             )
             
    for det in range(100):
        with app.app_context():
            OrderDetailsModel.create(
                random.randint(1,100),#order_detail_id = db.Column(db.Integer,primary_key = True) 
                random.randint(1,50),#orders_id = db.Column(db.Integer,db.ForeignKey("orders.orders_id"), unique=False, nullable = False)
                #order = db.relationship("OrdersModel", back_populates = "order_details")
                random.randint(1,25),#product_id = db.Column(db.Integer,db.ForeignKey("products.products_id"), unique = False, nullable = False)
                #product = db.relationship("ProductsModel", back_populates = "order_details")
                random.randint(1,5),#quantity = db.Column(db.Integer, unique = False, nullable = False)
                random.uniform(100,150),#unit_price = db.Column(db.Float(precision = 2))
                random.uniform(0.1,0.3),#discount = db.Column(db.Float(precision = 2))
                
            )

        
        
if __name__ == "__main__":
    insert_dummy_data()