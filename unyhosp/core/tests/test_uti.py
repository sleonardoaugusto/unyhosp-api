from django.test import TestCase
from unyhosp.test_utils.methods import ResourceMethods
from unyhosp.core import models
import json


class UTITest(TestCase, ResourceMethods):
    def setUp(self):
        self.resource = 'utis'
        h = models.Hospital.objects.create(name='Albert Einstein')
        self.data = {"name": "XPTO", "hospital": h.id}

    def test_get(self):
        """GET utis/ must return status code 200 """
        url = self._url(resource=self.resource)
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_post(self):
        """POST method must return status code 201"""
        url = self._url(resource=self.resource)
        response = self.client.post(url, self.data)
        self.assertEqual(201, response.status_code)

    def test_put(self):
        """PUT method must return status code 200"""
        url = self._url(resource=self.resource)
        _response = self.client.post(url, self.data)
        _response_data = json.loads(_response.content)
        url = self._url(resource=self.resource, pk=_response_data['id'])
        response = self.client.put(url, self.data, content_type='application/json')
        self.assertEqual(200, response.status_code)

    def test_delete(self):
        """DELETE method must reuturn status code 204"""
        url = self._url(resource=self.resource)
        _response = self.client.post(url, self.data)
        _response_data = json.loads(_response.content)
        url = self._url(resource=self.resource, pk=_response_data['id'])
        response = self.client.delete(url, self.data, content_type='application/json')
        self.assertEqual(204, response.status_code)
