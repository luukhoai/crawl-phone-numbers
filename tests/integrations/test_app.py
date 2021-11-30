import requests
from http import HTTPStatus

from tests import BaseTestCase


class IntegrationTestApp(BaseTestCase):

    def test_get_place_success(self):
        url = f'http://localhost:5000/getphonenumber?address={self.address}'
        response = requests.get(url)
        data = response.json()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['formatted_phone_number'], '(650) 810-1010')

    def test_not_input_address(self):
        url = 'http://localhost:5000/getphonenumber'
        response = requests.get(url)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_get_zero_result(self):
        url = 'http://localhost:5000/getphonenumber?address=asdasd'
        response = self.client.get(url)
        data = response.get_json()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(data), 0)
