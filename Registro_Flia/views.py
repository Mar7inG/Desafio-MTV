from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Registro_Flia.models import Familia

# Create your views here.

def Inicio(request):

    documento=f"<h1>PAGINA DE INICIO</h1>"
    return HttpResponse( documento)

def familia(sel,nombre, apellido, edad,documento,email ): 
    
    familia=Familia(nombre=nombre, apellido=apellido, edad=edad,documento=documento,email=email)
    familia.save()
    return HttpResponse(f""" 
    
     <p>Integrante de la familia {apellido} fue guardado.

    """)

