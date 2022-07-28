from django.db import models

# Create your models here.

class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)
    count=models.IntegerField(default='1')

    def __str__(self):
        return self.uuid