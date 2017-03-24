from django.test import TestCase
from django.core.urlresolvers import reverse as r

from rest_framework.test import APIClient
from rest_framework import status

from djangorest.api.models import Bucketlist


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

    def test_api_get_bucketlist(self):
        """Test the api can get a given bucketlist."""
        bucketlist = Bucketlist.objects.get()
        response = self.client.get(
            r('details', kwargs={'pk': bucketlist.id}),
            format='json'
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_update_bucketlist(self):
        """Test the api can update a given bucketlist."""
        bucketlist = Bucketlist.objects.get()
        change_bucketlist = {'name': 'Something new'}
        res = self.client.put(
            r('details', kwargs={'pk': bucketlist.id}),
            change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            r('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
