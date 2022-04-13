from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 32)
    author = models.CharField(max_length = 32)
    year = models.IntegerField()
    description = models.CharField(max_length = 140)