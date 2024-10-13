from django.db import models

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=100)
    country=models.CharField(max_length=100)

class Request(models.Model):
    published_date=models.DateField()
    out_city=models.CharField(max_length=100)
    to_city = models.CharField(max_length=100)
    user=models.CharField(max_length=100)