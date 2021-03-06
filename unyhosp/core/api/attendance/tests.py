from django.test import TestCase
from unyhosp.test_utils.methods import ResourceMethods
from unyhosp.core.api.hospital.model import Hospital
from unyhosp.core.api.pacient.model import Pacient
import json


class AttendanceTest(TestCase, ResourceMethods):
    def setUp(self):
        self.resource = 'attendances'
        self.url = self._url(resource=self.resource)
        h = Hospital.objects.create(name='Hospital - Albert Einstein')
        p = Pacient.objects.create(
            name='Romildo Ferrarezzi',
            document_id=45009877899,
            email='romildo.f@gmail.com',
            date_of_birth='1995-08-06'
        )
        self.data = {
            "entry_reason": "Lorem Ipsum",
            "hma": "Lorem Ipsum",
            "comorbidity": "Lorem Ipsum",
            "atb": "Lorem Ipsum",
            "hd": "Lorem Ipsum",
            "medicines_in_use": "Lorem Ipsum",
            "previous_pathologies": "Lorem Ipsum",
            "allergies": "Lorem Ipsum",
            "cultures": "Lorem Ipsum",
            "vasoactive_drugs": "Lorem Ipsum",
            "sedation": "Lorem Ipsum",
            "venous_access": "Lorem Ipsum",
            "diet": "Lorem Ipsum",
            "probes_and_drains": "Lorem Ipsum",
            "ventilation": "Lorem Ipsum",
            "complications": "Lorem Ipsum",
            "therapeutic_plan": "Lorem Ipsum",
            "hospital": h.id,
            "pacient": p.id
        }

    def test_get(self):
        """GET attendances/ must return status code 200 """
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
