from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Registro_Flia.models import Familia

# Create your views here.

def Inicio(request):

    documento=f"<h1>PAGINA DE INICIO</h1>"
    return HttpResponse( documento)

def familia(sel,nombre, apellido, edad,documento,email,fecha_nac=None ): 
    
    familia=Familia(nombre=nombre, apellido=apellido, edad=edad,documento=documento,email=email,fecha_nac=fecha_nac)
    familia.save()
    return HttpResponse(f""" 
    
     <p>Integrante de la familia {apellido} fue guardado.

    """)

def lista_familiares(self):
    
    listaflia=Familia.objects.all()

    return render(self,"Template_1.html",{"itegrantes_flia":listaflia})
