from unittest import TestCase

from app import create_app


app = create_app(environment='testing')


class BaseTestCase(TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.app_ctx = app.app_context()
        self.app_ctx.push()
        self.address = 'Computer History Museum Mountain View USA'

    def tearDown(self):
        self.app_ctx.pop()
