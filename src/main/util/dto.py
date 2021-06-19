from flask_restx import Namespace, fields


class SowDto:
    api = Namespace(
        'sow', description='sow related operations')
    sow = api.model('sow', {
        'date': fields.Date(required=True, description='partial form'),
        'plot': fields.String(required=True, description='partial form'),
        'crop': fields.String(required=True, description='partial form'),
        'quantity': fields.Integer(required=True, description='partial form'),
        'time_to_harvest': fields.String(required=True, description='partial form'),
        'harvest_duration': fields.String(required=True, description='partial form'),
        'expected_yield': fields.String(required=True, description='partial form'),
    })


class PlotDto:
    api = Namespace('plot', description='plot related operations')
    plot = api.model('plot', {
        'name': fields.String(required=True, description='plot name and identifier'),
        'area': fields.Float(required=True, description='area of the plot'),
    })


class HarvestDto:
    api = Namespace('harvesting_form',
                    description='harvesting_form related operations')
    harvesting_form = api.model('harvesting_form', {
        'date': fields.Date(required=True, description='partial form'),
        'plot': fields.Integer(required=True, description='partial form'),
        'quantity': fields.Integer(required=True, description='partial form'),
        'harvest_quantity': fields.String(required=True, description='partial form'),
    })


class IssueDto:
    api = Namespace('issue_form',
                    description='issue_form related operations')
    issue_form = api.model('issue_form', {
        'date': fields.Date(required=True, description='partial form'),
        'plot': fields.Integer(required=True, description='partial form'),
        'issue_type': fields.Integer(required=True, description='partial form'),
        'description': fields.String(required=True, description='partial form'),
    })


class ApplicationDto:
    api = Namespace('application_form',
                    description='application_form related operations')

    application_form = api.model('application_form', {
        'date': fields.Date(required=True, description='partial form'),
        'plot': fields.Integer(required=True, description='partial form'),
        'product': fields.String(required=True, description='partial form'),
        'quantity': fields.Integer(required=True, description='partial form'),
        'dose': fields.Float(required=True, description='partial form'),
        'machine': fields.String(required=True, description='partial form'),
    })
