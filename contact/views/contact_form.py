from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )

def create(request):
    if request.method == 'POST':
        context = {
            'form':ContactForm(request.POST)
        }
        return render(
            request,
            'contact/create.html',
            context,
            )

    context = {
        'form':ContactForm()
    }
    return render(
        request,
        'contact/create.html',
        context,
        )



