from flask_restx import fields
from flask_restx.reqparse import RequestParser
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.stores_model import StoreModel


class StoreRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=10, location='args')
        return parser

    def create(self):
        return self.namespace.model('Store Create', {
            'stand': fields.String(required=True, min_length=1, max_length=3),
            'name': fields.String(required=True, min_length=1, max_length=100),
            'logo': fields.String(required=False),
            'phone': fields.String(required=False),
            'days_open': fields.String(required=False),
            'schedule': fields.String(required=False),
            'level': fields.String(required=False),
            'title': fields.String(required=False),
            'description': fields.String(required=False),
            'photo_menu_1': fields.String(required=False),
            'photo_menu_2': fields.String(required=False),
            'photo_menu_3': fields.String(required=False),
            'photo_primary': fields.String(required=False)

        })

    def update(self):
        return self.namespace.model('Store Update', {
            'stand': fields.String(required=True, min_length=1, max_length=3),
            'name': fields.String(required=True, min_length=1, max_length=100),
            'logo': fields.String(required=False),
            'phone': fields.String(required=False),
            'days_open': fields.String(required=False),
            'schedule': fields.String(required=False),
            'level': fields.String(required=False),
            'title': fields.String(required=False),
            'description': fields.String(required=False),
            'photo_menu_1': fields.String(required=False),
            'photo_menu_2': fields.String(required=False),
            'photo_menu_3': fields.String(required=False),
            'photo_primary': fields.String(required=False)
        })


class StoreResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = StoreModel
