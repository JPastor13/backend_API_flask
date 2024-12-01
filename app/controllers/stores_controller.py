from app import db
from app.models.stores_model import StoreModel
from app.schemas.stores_shema import StoreResponseSchema
from http import HTTPStatus


class StoreController:
    def __init__(self):
        self.db = db
        self.model = StoreModel
        self.schema = StoreResponseSchema

    def fetch_all(self, query_params):
        try:
            page = query_params['page']
            per_page = query_params['per_page']

            records = self.model.where(status=True).order_by('id').paginate(
                page=page,
                per_page=per_page
            )
            stores = self.schema(many=True)
            return {
                'results': stores.dump(records.items),
                'pagination': {
                    'totalRecords': records.total,
                    'totalPages': records.pages,
                    'perPage': records.per_page,
                    'currentPage': records.page
                }
            }, HTTPStatus.OK
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def save(self, body):
        try:
            record_new = self.model.create(**body)
            self.db.session.add(record_new)
            self.db.session.commit()
            return {
                'message': f'La tienda {body["name"]} se creo con exito'
            }, HTTPStatus.CREATED
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def find_by_id(self, id):
        try:
            record = self.model.where(id=id,status=True).first()

            if record:
                store = self.schema(many=False)
                return {
                    'record': store.dump(record)
                }, HTTPStatus.OK

            return {
                'message': f'No se encontro la tienda {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def update(self, id, body):
        try:
            record = self.model.where(id=id,status=True).first()

            if record:
                record.update(**body)
                self.db.session.add(record)
                self.db.session.commit()

                return {
                    'message': f'La tienda {id}, ha sido actualizado.'
                }, HTTPStatus.OK

            return {
                'message': f'No se encontro la tienda {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR

    def remove(self, id):
        try:
            record = self.model.where(id=id,status=True).first()

            if record:
                record.update(status=False)
                self.db.session.add(record)
                self.db.session.commit()

                return {
                    'message': f'La tienda {id}, ha sido removido.'
                }, HTTPStatus.OK

            return {
                'message': f'No se encontro la tienda {id}'
            }, HTTPStatus.NOT_FOUND
        except Exception as e:
            self.db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'reason': str(e)
            }, HTTPStatus.INTERNAL_SERVER_ERROR
