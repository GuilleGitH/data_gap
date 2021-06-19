from flask import request
from flask_restx import Resource

from ..util.dto import PlotDto
from ..service.plot_service import new_plot, get_all, get_by_id

api = PlotDto.api
_plot = PlotDto.plot


@api.route('/')
class PlotController(Resource):
    @api.response(201, 'New plot created successfully.')
    @api.doc('Plot related endpoints')
    @api.expect(_plot, validate=True)
    def post(self):
        """Adds a new plot to the database."""
        data = request.json
        return new_plot(data)

    @api.marshal_list_with(_plot, envelope='data')
    def get(self):
        """Get a list of all plots in the database."""
        return get_all()
