from django.conf import settings
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    description = models.TextField(max_length=400)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True)

    def update(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title