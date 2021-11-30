from http import HTTPStatus
from unittest.mock import patch
from tests import BaseTestCase
from tests import mocks


class UnittestTestApp(BaseTestCase):

    def test_not_input_address(self):
        url = '/getphonenumber'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_get_empty_address(self):
        url = '/getphonenumber?address='
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    @patch('app.services.google_place.requests.get', side_effect=mocks.mock_get_place_success)
    def test_get_phone_numb_success(self, *args):
        url = '/getphonenumber?address={}'.format(self.address)
        response = self.client.get(url)
        data = response.get_json()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['formatted_phone_number'], '(650) 810-1010')

    @patch('app.services.google_place.requests.get', side_effect=mocks.mock_get_place_zero_result)
    def test_get_place_zero_result(self, *args):
        url = '/getphonenumber?address={}'.format(self.address)
        response = self.client.get(url)
        data = response.get_json()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(data), 0)

    @patch('app.services.google_place.requests.get', side_effect=mocks.mock_get_place_invalid)
    def test_get_place_invalid(self, *args):
        url = '/getphonenumber?address={}'.format(self.address)
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    @patch('app.services.google_place.requests.get', side_effect=mocks.mock_get_place_internal)
    def test_get_place_internal(self, *args):
        url = '/getphonenumber?address={}'.format(self.address)
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    @patch('app.services.google_place.requests.get', side_effect=mocks.mock_get_place_raise_exception)
    def test_get_place_raise_exception(self, *args):
        url = '/getphonenumber?address={}'.format(self.address)
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    @patch('app.services.google_place.requests.get', side_effect=mocks.mock_get_detail_zero_result)
    def test_get_detail_zero_result(self, *args):
        url = '/getphonenumber?address={}'.format(self.address)
        response = self.client.get(url)
        data = response.get_json()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(data), 0)

    @patch('app.services.google_place.requests.get', side_effect=mocks.mock_get_detail_not_found)
    def test_get_detail_not_found(self, *args):
        url = '/getphonenumber?address={}'.format(self.address)
        response = self.client.get(url)
        data = response.get_json()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(data), 0)

    @patch('app.services.google_place.requests.get', side_effect=mocks.mock_get_detail_invalid)
    def test_get_detail_invalid(self, *args):
        url = '/getphonenumber?address={}'.format(self.address)
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    @patch('app.services.google_place.requests.get', side_effect=mocks.mock_get_detail_internal)
    def test_get_detail_internal(self, *args):
        url = '/getphonenumber?address={}'.format(self.address)
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.INTERNAL_SERVER_ERROR)

    @patch('app.services.google_place.requests.get', side_effect=mocks.mock_get_detail_raise_exception)
    def test_get_detail_raise_exception(self, *args):
        url = '/getphonenumber?address={}'.format(self.address)
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    @patch('app.services.google_place.GoogleFindPhone.find_phone_number_from_text',
           side_effect=mocks.mock_raise_marshmallow_exeption)
    def test_get_raise_marshmallow_error(self, *args):
        url = '/getphonenumber?address={}'.format(self.address)
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
