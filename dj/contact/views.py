from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def contact (request):
    template = loader.get_template('contact.html')
    context = {}
    return HttpResponse(template.render(context, request))