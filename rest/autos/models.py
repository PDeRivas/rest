from django.db import models

# Create your models here.
class Auto(models.Model):
    nombre = models.CharField(max_length=200)
    anio = models.IntegerField()