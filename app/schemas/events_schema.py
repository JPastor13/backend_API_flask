from flask_restx import fields
from flask_restx.reqparse import RequestParser
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.events_model import EventModel


class EventRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=10, location='args')
        return parser

    def create(self):
        return self.namespace.model('Event Create', {
            'title': fields.String(required=True, min_length=1, max_length=150),
            'photo': fields.String(required=False),
            'fecha': fields.String(required=False),
            'hora': fields.String(required=False)
        })

    def update(self):
        return self.namespace.model('Event Update', {
            'title': fields.String(required=True, min_length=1, max_length=150),
            'photo': fields.String(required=False),
            'fecha': fields.String(required=False),
            'hora': fields.String(required=False)
        })


class EventResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = EventModel
