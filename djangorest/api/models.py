from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver


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


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
