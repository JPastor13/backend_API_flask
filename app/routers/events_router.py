from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.controllers.events_controller import EventController
from app.schemas.events_schema import EventRequestSchema


event_ns = api.namespace(
    name='Events',
    description='Endpoints del modulo Events',
    path='/events'
)

request_schema = EventRequestSchema(event_ns)


@event_ns.route('')
@event_ns.doc(security='Bearer')
class EventsListCreate(Resource):
    #@jwt_required()
    @event_ns.expect(request_schema.all())
    def get(self):
        ''' Listar todos eventos '''
        query_params = request_schema.all().parse_args()
        controller = EventController()
        return controller.fetch_all(query_params)

    @jwt_required()
    @event_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creacion de un evento '''
        controller = EventController()
        return controller.save(request.json)


@event_ns.route('/<int:id>')
@event_ns.doc(security='Bearer')
class EventsGetUpdateDelete(Resource):
    #@jwt_required()
    def get(self, id):
        ''' Obtener el evento por su id '''
        controller = EventController()
        return controller.find_by_id(id)

    @jwt_required()
    @event_ns.expect(request_schema.update(), validate=True)
    def patch(self, id):
        ''' Actualizar el evento por su id '''
        controller = EventController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Eliminar el evento por su id '''
        controller = EventController()
        return controller.remove(id)
