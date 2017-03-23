from rest_framework import serializers

from .models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_updated')
        read_only_fields = ('date_created', 'date_updated')
