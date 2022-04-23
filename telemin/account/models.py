from django.db import models
from django.conf import settings

from . import services


class Telegram_Channels(models.Model):
    pass


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.FileField(upload_to=services.user_photo_size_verify, blank=True)
