from marshmallow import Schema, fields


class PlainCustomerSchema(Schema):
    customer_id = fields.Int(dump_only=True)
    first_name = fields.Str()
    last_name = fields.Str()
    company_name = fields.Str()
    billing_address = fields.Str()
    city = fields.Str()
    state_or_province = fields.Str()
    zip_code = fields.Str()
    email = fields.Str()
    company_website = fields.Str()
    phone_number = fields.Str()
    fax_number = fields.Str()
    ship_address = fields.Str()
    ship_city = fields.Str()
    ship_state_or_province = fields.Str()
    ship_zip_code = fields.Str()
    ship_phone_number = fields.Str()


class PlainProductSchema(Schema):
    product_id = fields.Int(dump_only=True)
    product_name = fields.Str(required=True)
    unit_price = fields.Float(required=True)


class PlainEmployeeSchema(Schema):
    employee_id = fields.Int(dump_only=True)
    first_name = fields.Str()
    last_name = fields.Str()
    title = fields.Str()


class PlainShippingSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class PaymentSchema(PlainProductSchema):
    id = fields.Int(dump_only=True)
    total = fields.Float()
