from django.db import models


# Create your models here.

class UUIDModel(models.Model):
    updated = models.DateTimeField(auto_now_add=True)
    uuid = models.CharField(max_length=400)
