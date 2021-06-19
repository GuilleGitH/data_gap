from flask import request
from flask_restx import Resource
from ..util.dto import SowDto
from ..service.sow_service import save_new_sow, get_all_sow, get_join

api = SowDto.api
_sow = SowDto.sow


@api.route('/')
class SowController(Resource):
    @api.response(201, 'Sow created successfully')
    @api.doc('Sow related enpoints')
    @api.expect(_sow, validate=True)
    def post(self):
        """Adds a new Sow to the database"""
        data = request.json
        return save_new_sow(data)

    @api.marshal_list_with(_sow, envelope='data')
    def get(self):
        """Get a list of all sows in the database"""
        return get_all_sow()


@api.route('/test')
class Sow(Resource):
    @api.response(201, 'Sow created successfully')
    @api.doc('Sow related enpoints')
    # @api.marshal_list_with(_sow, envelope='data')
    def get(self):
        """Get a list of all sows in the database"""
        return get_join()
