from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_cors import CORS
from app.config import environment
import cloudinary
from cloudinary.uploader import upload

from app.config import environment


app = Flask(__name__)
app.config.from_object(environment)
CORS(app, supports_credentials=True)#cors sea público
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
##sgsgsgsgd
db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
mail = Mail(app)
