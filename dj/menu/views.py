from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Platillo, Categoria
def menu (request):
    menu_list = Platillo.objects.all()
    cat_list = Categoria.objects.all()
    #Archivo HTML con template
    template = loader.get_template('menu.html')
    #logica de la vista
    context = {
            "menu_list": menu_list,
            "cat_list": cat_list
    }
    #respuesta
    return HttpResponse(template.render(context,request))
