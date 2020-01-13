from django.test import TestCase
from unyhosp.test_utils.methods import ResourceMethods

import json


class HospitalTest(TestCase, ResourceMethods):
    def setUp(self):
        self.data = {"name": "Albert Einstein"}
        self.resource = 'hospitals'
        self.url = self._url(resource=self.resource)

    def test_get(self):
        """GET hospitals/ must return status code 200 """
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    def test_post(self):
        """POST method must return status code 201"""
        response = self.client.post(self.url, self.data)
        self.assertEqual(201, response.status_code)

    def test_put(self):
        """PUT method must return status code 200"""
        _response = self.client.post(self.url, self.data)
        _response_data = json.loads(_response.content)
        url = self._url(resource=self.resource, pk=_response_data.get('id'))
        response = self.client.put(url, self.data, content_type='application/json')
        self.assertEqual(200, response.status_code)

    def test_delete(self):
        """DELETE method must reuturn status code 204"""
        _response = self.client.post(self.url, self.data)
        _response_data = json.loads(_response.content)
        url = self._url(resource=self.resource, pk=_response_data.get('id'))
        response = self.client.delete(url, self.data, content_type='application/json')
        self.assertEqual(204, response.status_code)
