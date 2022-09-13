from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields  = [
            'nombre_cliente',
            'correo_cliente',
            'telefono_cliente',
            'mensaje_cliente'
        ]
    
