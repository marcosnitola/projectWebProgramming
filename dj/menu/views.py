from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def menu (request):
    #Archivo HTML con template
    template = loader.get_template('menu.html')
    #logica de la vista
    context = {}
    #respuesta
    return HttpResponse(template.render(context,request))
