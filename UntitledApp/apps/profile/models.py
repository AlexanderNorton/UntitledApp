from email.mime import image
from django.conf import settings
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.shortcuts import get_object_or_404


class Profile(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    url_tag = models.CharField(max_length=400, unique=True)
    title = models.CharField(max_length=400)
    description = models.TextField(
        max_length=400, default="This is a description")
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_pictures', blank=True)

    def update(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


def save_profile(sender, instance, created, **kwargs):
    if created:
        obj = Profile.objects.create(
            owner=instance, title=instance, url_tag=instance)
    else:
        Profile.objects.filter(owner=instance).update(
            updated_date=timezone.now())


post_save.connect(save_profile, sender=User)
