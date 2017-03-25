from django.conf import settings
from django.db import models


class Bucketlist(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='bucketlists',
        on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
