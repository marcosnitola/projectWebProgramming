from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render

from .models import ContactMessage
from .forms import ContactForm
def contact (request):
    template = loader.get_template('contact.html')
    if request.POST:
        newmessage = ContactMessage(
                nombre_cliente = request.POST["nombres"],
                correo_cliente = request.POST["correo"],
                telefono_cliente = request.POST["celular"],
                mensaje_cliente = request.POST["mensaje"],
        )
        newmessage.save()
    #form = ContactForm(request.POST or None)
    #if form.is_valid():
    #    form.save()
    #    return redirect('')
    context = {
        #"form": form
    }
    #return HttpResponse(template.render(context, request))
    return render(request,'contact.html', context)
