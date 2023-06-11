from django.shortcuts import render
from contact.models import Contact

def home(request):
    contacts = Contact.objects.all()
    context = {
        'contacts':contacts,
    }
    return render(
        request,
        'contact/index.html',
        context,
        )