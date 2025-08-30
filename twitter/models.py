from django.db import models
from django.utils import timezone


class TwitterProduct(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
