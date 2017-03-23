from django.test import TestCase
from django.core.urlresolvers import reverse as r

from rest_framework.test import APIClient
from rest_framework import status


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Disneylandia'}
        self.response = self.client.post(
            r('create'),
            self.bucketlist_data,
            format='json'
            )

    def test_api_create_bucketlist(self):
        """Test the api has bucket creation capability"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
