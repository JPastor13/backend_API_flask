from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.controllers.promotions_controller import PromotionController
from app.schemas.promotions_schema import PromotionRequestSchema


promotion_ns = api.namespace(
    name='Promotions',
    description='Endpoints del modulo Promotions',
    path='/promotions'
)

request_schema = PromotionRequestSchema(promotion_ns)


@promotion_ns.route('')
@promotion_ns.doc(security='Bearer')
class PromotionsCreate(Resource):
    @jwt_required()
    @promotion_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creacion de una nueva promoción '''
        controller = PromotionController()
        return controller.save(request.json)


@promotion_ns.route('/<int:store_id>')
@promotion_ns.doc(security='Bearer')
class PromotionsList(Resource):
    #@jwt_required()
    @promotion_ns.expect(request_schema.all())
    def get(self, store_id):
        ''' Listar todas las promociones '''
        query_params = request_schema.all().parse_args()
        controller = PromotionController()
        return controller.fetch_all(store_id, query_params)

@promotion_ns.route('/<int:id>')
@promotion_ns.doc(security='Bearer')
class PromotionsGetUpdateDelete(Resource):
    #@jwt_required()
    def get(self, id):
        ''' Obtener la promoción por su id '''
        controller = PromotionController()
        return controller.find_by_id(id)

    @jwt_required()
    @promotion_ns.expect(request_schema.update(), validate=True)
    def patch(self, id):
        ''' Actualizar la promoción por su id '''
        controller = PromotionController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Eliminar la promoción por su id '''
        controller = PromotionController()
        return controller.remove(id)
