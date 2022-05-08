from django.contrib.auth.models import User
from django.db import models

from .validations import validation_profile_image


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')
    avatar = models.ImageField(upload_to=validation_profile_image, null=True, blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(max_length=100, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, related_name='profile_city', null=True, blank=True)

    def __str__(self):
        return 'Profile {}'.format(self.user)
