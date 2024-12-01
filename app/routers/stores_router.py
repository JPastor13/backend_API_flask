from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.controllers.stores_controller import StoreController
from app.schemas.stores_shema import StoreRequestSchema


store_ns = api.namespace(
    name='Stores',
    description='Endpoints del modulo Stores',
    path='/stores'
)

request_schema = StoreRequestSchema(store_ns)


@store_ns.route('')
@store_ns.doc(security='JPastor')
class StoressListCreate(Resource):
    @jwt_required()
    @store_ns.expect(request_schema.all())
    def get(self):
        ''' Listar todas las tiendas '''
        query_params = request_schema.all().parse_args()
        controller = StoreController()
        return controller.fetch_all(query_params)

    @jwt_required()
    @store_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creacion de una tienda '''
        controller = StoreController()
        return controller.save(request.json)


@store_ns.route('/<int:id>')
@store_ns.doc(security='JPastor')
class StoresGetUpdateDelete(Resource):
    #@jwt_required()
    def get(self, id):
        ''' Obtener la tienda por su id '''
        controller = StoreController()
        return controller.find_by_id(id)

    #@jwt_required()
    @store_ns.expect(request_schema.update(), validate=True)
    def patch(self, id):
        ''' Actualizar la tienda por su id '''
        controller = StoreController()
        return controller.update(id, request.json)

    #@jwt_required()
    def delete(self, id):
        ''' Eliminar la tienda por su id '''
        controller = StoreController()
        return controller.remove(id)
