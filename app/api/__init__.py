from flask import Blueprint
from flask_restful import Api
from marshmallow.exceptions import MarshmallowError
from requests.exceptions import RequestException

from .main_api import MainApiResource
from .healthcheck import HealthCheck
from ..common.error_handling import handle_validation_error


class MainApi(Api):

    def handle_error(self, e):
        '''Handle API exceptions'''
        if isinstance(e, MarshmallowError):
            setattr(e, 'description', str(e))
            return handle_validation_error(e)
        elif isinstance(e, RequestException):
            setattr(e, 'description', str(e))
            return handle_validation_error(e)
        raise e


api_bp = Blueprint('main', __name__)


main_api = MainApi(api_bp)


main_api.add_resource(MainApiResource, '/getphonenumber')
main_api.add_resource(HealthCheck, '/healthcheck')
