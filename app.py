from resources.customers import blp as CustomerBlueprint
from flask_smorest import Api
from flask_migrate import Migrate
from flask import Flask
from db import db
from dotenv import load_dotenv


load_dotenv()


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Beranda Toko REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(CustomerBlueprint)
    return app
