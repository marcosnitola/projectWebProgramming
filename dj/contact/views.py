from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render

from .models import ContactMessage
from .forms import ContactForm
def contact (request):
    template = loader.get_template('contact.html')
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('')
    context = {
        "form": form
    }
    return HttpResponse(template.render(context, request))
    # return render(request,'contact.html', context)
