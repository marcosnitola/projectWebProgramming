from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader



def index(request):
    #Archivo HTML con template
    template = loader.get_template('index.html')
    #logica de la vista
    context = {}
    #respuesta
    return HttpResponse(template.render(context,request))

def map (request):
    template = loader.get_template('map.html')
    context = {}
    return HttpResponse(template.render(context, request))

def order (request):
    template = loader.get_template('order.html')
    context = {}
    return HttpResponse(template.render(context, request))

def contact (request):
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context, request))

