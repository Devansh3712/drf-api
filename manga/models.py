from datetime import datetime

from django.db import models


# Create your models here.
class Manga(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    chapters = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    added_on = models.DateTimeField(default=datetime.now())

    class Meta:
        ordering = ("name",)
