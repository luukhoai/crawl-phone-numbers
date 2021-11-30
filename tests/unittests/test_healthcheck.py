from http import HTTPStatus
from tests import BaseTestCase


class HealthcheckTestApp(BaseTestCase):

    def test_healthcheck(self):
        url = '/healthcheck'
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
