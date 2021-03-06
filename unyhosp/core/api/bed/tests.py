from django.test import TestCase
from unyhosp.test_utils.methods import ResourceMethods
from unyhosp.core.api.hospital.model import Hospital
from unyhosp.core.api.uti.model import UTI
from unyhosp.core.api.pacient.model import Pacient
import json


class BedTest(TestCase, ResourceMethods):
    def setUp(self):
        self.resource = 'beds'
        self.url = self._url(resource=self.resource)
        h = Hospital.objects.create(name='Hospital - Albert Einstein')
        u = UTI.objects.create(name='UTI - XPTO', hospital=h)
        p = Pacient.objects.create(
            name='Romildo Ferrarezzi',
            document_id=45009877899,
            email='romildo.f@gmail.com',
            date_of_birth='1995-08-06'
        )
        self.data = {"name": "Bed - XYZ", "uti": u.id, "pacient": p.id}

    def test_get(self):
        """GET beds/ must return status code 200 """
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
