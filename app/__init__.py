from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from app.config import environment


app = Flask(__name__)
app.config.from_object(environment)

authorization = {
    'JPastor': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    app,
    title='API Plaza Santander',
    version='0.1',
    description='RESTAPI de plaza santander en Flask por Richard Pastor',
    doc='/swagger-ui',
    authorizations=authorization
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
mail = Mail(app)
