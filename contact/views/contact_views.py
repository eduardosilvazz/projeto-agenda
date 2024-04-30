from django.shortcuts import render
from contact.models import Contact
from django.http import Http404

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[10:20]
    
    print(contacts.query)

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }
    
    return render(request, 'contact/index.html', context)


def contact(request, contact_id):
    single_contact = Contact.objects.filter(pk=contact_id).first()
    
    if single_contact is None:
        raise Http404()

    contact_name = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': contact_name
    }
    
    return render(request, 'contact/contact.html', context)

def search(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[10:20]

    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }
    
    return render(request, 'contact/index.html', context)


