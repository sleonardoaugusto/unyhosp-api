from django.test import TestCase
from unyhosp.test_utils.methods import ResourceMethods
from unyhosp.core.api.hospital.model import Hospital
from unyhosp.core.api.bed.model import Bed
import json


class UTITest(TestCase, ResourceMethods):
    def setUp(self):
        self.resource = 'utis'
        self.url = self._url(resource=self.resource)
        h = Hospital.objects.create(name='Albert Einstein')
        self.data = {"name": "XPTO", "hospital": h.id}

    def test_get(self):
        """GET utis/ must return status code 200 """
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

    def test_bed_create(self):
        """POST method should create 10 beds"""
        _response = self.client.post(self.url, self.data)
        _response_data = json.loads(_response.content)
        uti_id = _response_data.get('id')
        bed_qty = len(Bed.objects.filter(uti__exact=uti_id))
        self.assertEqual(bed_qty, 10)
