from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Platillo, Categoria
def menu (request):
    menu_list = Platillo.objects.all()
    comida_list = Platillo.objects.filter(tipo=2)
    bebida_list = Platillo.objects.filter(tipo=1)
    cat_list = Categoria.objects.all()

    #Archivo HTML con template
    template = loader.get_template('menu.html')
    #logica de la vista
    context = {
            "menu_list": menu_list,
            "comida_list": comida_list,
            "bebida_list": bebida_list,
            "cat_list": cat_list
    }
    #respuesta
    return HttpResponse(template.render(context,request))
