from __future__ import unicode_literals

from django.db import models

# Create your models here.
class result(models.Model):
    review=models.TextField(null=False,max_length=500)
    prediction=models.IntegerField()
    sentiment=models.IntegerField()

    def __str__(self):
        return self.review