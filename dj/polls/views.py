from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


from menu.models import Platillo
def index(request):
    # Seleccionamos los platillos más populares del menú 
    platospopulares = Platillo.objects.order_by('popularidad')[::-1][:6]
    #Archivo HTML con template
    template = loader.get_template('index.html')
    #logica de la vista
    context = {
            'platillos_populares': platospopulares
    }
    #respuesta
    return HttpResponse(template.render(context,request))

def map (request):
    template = loader.get_template('map.html')
    context = {}
    return HttpResponse(template.render(context, request))

