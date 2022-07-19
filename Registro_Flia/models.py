from django.db import models

# Create your models here.

class Familia(models.Model):

    nombre=models.CharField(max_length=40,blank=True )
    apellido=models.CharField(max_length=40,blank=True )
    documento=models.IntegerField(blank=True )
    edad=models.IntegerField(blank=True )
    email=models.EmailField(max_length=40,blank=True )
    fecha_nac=models.DateField(null=True,blank=True )
    