from django.test import TestCase
from unyhosp.test_utils.methods import ResourceMethods
from unyhosp.core.services.hospital.model import Hospital
from unyhosp.core.services.uti.model import UTI
from unyhosp.core.services.pacient.model import Pacient
import json


class BedTest(TestCase, ResourceMethods):
    def setUp(self):
        self.resource = 'beds'
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
