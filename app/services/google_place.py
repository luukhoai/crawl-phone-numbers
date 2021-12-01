import requests
from flask import current_app as app
from werkzeug.exceptions import BadRequest, InternalServerError


class GoogleFindPhone(object):

    def __init__(self):
        self.url = 'https://maps.googleapis.com/maps/api/place/{}/json?key={}&{}'

    def _find_candidates_from_text(self, text):
        '''
        Find candidates from text input
        Parameters:
            text: str, address text in query input
        Return:
            List of candidates, which contain place_ids.
            If requests's Status is INVALID_REQUEST, OVER_QUERY_LIMIT,
                REQUEST_DENIED, UNKNOWN_ERROR. Raise exception
        '''
        url = self.url.format(
            'findplacefromtext', app.config['API_KEY'],
            f'input={text}&inputtype=textquery')
        app.logger.info(url)
        response = requests.get(url).json()
        if response['status'] == 'OK':
            return response['candidates']
        elif response['status'] == 'ZERO_RESULTS':
            app.logger.info(f'Not found any place_id with address: {text}')
            return []
        error_message = response.get('error_message', None)
        if response['status'] == 'INVALID_REQUEST':
            raise BadRequest(error_message)
        else:
            raise InternalServerError(error_message)

    def _find_phone_numb_from_place_id(self, place_id):
        '''
        Find phone number from place_id.
        Parameters:
            place_id: str, Google Place's Id
        Return:
            Return phone number if exists
            If requests's Status is INVALID_REQUEST, OVER_QUERY_LIMIT,
                REQUEST_DENIED, UNKNOWN_ERROR. Raise exception
        '''
        url = self.url.format(
            'details', app.config['API_KEY'],
            f'place_id={place_id}&fields=formatted_phone_number')
        app.logger.info(url)
        response = requests.get(url).json()
        if response['status'] == 'OK':
            return response['result']
        elif response['status'] in ['ZERO_RESULTS', 'NOT_FOUND']:
            app.logger.info(f'Not found phone_number with place_id: {place_id}')
            return False
        error_message = response.get('error_message', None)
        if response['status'] == 'INVALID_REQUEST':
            raise BadRequest(error_message)
        else:
            raise InternalServerError(error_message)

    def find_phone_number_from_text(self, text):
        '''
        Find phone numbers from text
        Parameters:
            text: str, address text in query input
        Return:
            List of phone numbers
        '''
        phone_numbers = []
        candidates = self._find_candidates_from_text(text)
        for candidate in candidates:
            phone = self._find_phone_numb_from_place_id(candidate['place_id'])
            if phone:
                phone_numbers.append(phone)
        return phone_numbers
