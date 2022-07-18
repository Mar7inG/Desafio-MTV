from django.db import models

# Create your models here.

class Familia(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    documento=models.IntegerField()
    edad=models.IntegerField()
    email=models.EmailField(max_length=40)
    fecha_nac=models.DateField(null=True)
    