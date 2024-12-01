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
#Configure Cloudinary
cloudinary.config(
cloud_name="dsuwaebrk",
api_key="422682953915149",
api_secret="QytDxda5S5vfPAj8BtTaadf-wm8"
)
@app.route('/upload',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error':'No file part'})
    file =request.files['file']
    if file.filename=='':
        return jsonify ({'error':'No selected file'})
    try:
        result=upload(file)
        return jsonify({'url': result['secure_url']})
    except Exception as e:
        return jsonify({'error':str(e)})
if __name__=='__main__':
    app.run(debug=True)
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
    description='RESTAPI de plaza santander en Flask',
    doc='/swagger-ui',
    authorizations=authorization
)
##sgsgsgsgd
db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
mail = Mail(app)
