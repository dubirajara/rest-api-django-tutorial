from django.test import TestCase
from django.contrib.auth.models import User
from djangorest.api.models import Bucketlist


class ModelTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="John")
        self.name = 'Write world class code'
        self.bucketlist = Bucketlist(name=self.name, owner=user)

    def test_model_create_bucketlist(self):
        """Test the bucketlist model can create a bucketlist"""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_tags_cant_be_blank(self):
        """Check name field cant be blank"""
        field = Bucketlist._meta.get_field('name')
        self.assertFalse(field.blank)

    def test_str(self):
        """Check __str__ return name field"""
        self.assertEqual('Write world class code', str(self.name))
