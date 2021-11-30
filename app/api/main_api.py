from http import HTTPStatus
from flask import current_app as app
from flask_restful import Resource
from webargs.flaskparser import use_args

from ..schema import AddressQuerySchema
from ..services.google_place import GoogleFindPhone


class MainApiResource(Resource):

    def __init__(self, *args, **kwargs):
        super(MainApiResource, self).__init__(*args, **kwargs)
        self.find_phone = GoogleFindPhone()

    @use_args(AddressQuerySchema, location="query")
    def get(self, args):
        '''
        GET api to find phone from address
        Parameters:
            args: dict, contain address information. Eg: {'address': 'address'}
        Return:
            A list contains phone numbers.
            Eg: [{'formatted_phone_number': '(650) 810-1010'}]
        '''
        address = args['address']
        app.logger.info(f'address: {address}')
        results = self.find_phone.find_phone_number_from_text(address)
        return results, HTTPStatus.OK
