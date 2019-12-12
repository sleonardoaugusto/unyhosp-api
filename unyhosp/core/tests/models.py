from django.test import TestCase


class ResponseTest(TestCase):
    def setup(self):
        self.response = self.client.get('/hospitals')

    def test_get_hospitals(self):
        """GET hospitals/ must return status code 200 """
        self.assertEqual(200, self.response.status_code)
