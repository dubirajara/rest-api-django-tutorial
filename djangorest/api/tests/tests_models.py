from django.test import TestCase
from djangorest.api.models import Bucketlist


class ModelTestCase(TestCase):
    def setUp(self):
        self.bucketlist_name = 'Write world class code'
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

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
        self.assertEqual('Write world class code', str(self.bucketlist_name))
