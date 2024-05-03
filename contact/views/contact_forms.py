from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator

from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone'
        )


def create(request):
    context = {
        'form': ContactForm()
    }
    
    context = {


    }
    return render(request, 'contact/create.html', context)