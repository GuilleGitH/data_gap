from flask_restx import Api
from flask import Blueprint

from .main.controller.sow_controller import api as sowing_sql
from .main.controller.plot_controller import api as plot_sql

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='GAP-A-FARM WEB-SERVICE',
          version='1.0',
          description='restx web service'
          )

api.add_namespace(sowing_sql, path='/sowing_sql')
api.add_namespace(plot_sql, path='/plot_sql')
