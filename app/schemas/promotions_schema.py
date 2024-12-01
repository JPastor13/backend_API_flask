from flask_restx import fields
from flask_restx.reqparse import RequestParser
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow.fields import Nested
from app.models.promotions_model import PromotionModel


class PromotionRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=10, location='args')
        return parser

    def create(self):
        return self.namespace.model('Promotion Create', {
            'store_id': fields.Integer(required=True),
            'title': fields.String(required=True, min_length=1, max_length=150),
            'photo': fields.String(required=False)            
        })

    def update(self):
        return self.namespace.model('Promotion Update', {
            'store_id': fields.Integer(required=True),
            'title': fields.String(required=True, min_length=1, max_length=150),
            'photo': fields.String(required=False)
        })


class PromotionResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PromotionModel
        include_fk = True
    store = Nested('StoreResponseSchema', many=False)