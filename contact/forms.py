from contact import models
from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class':'classe-first_name',
                'placeholder':'Write your first name'
            }
        ),
    )

    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'placeholder':'Write your middle name'
            }
        ),
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )
    
#Serve para fazermos algumas alterações ou validações dos dados antes dos mesmo serem enviados para o servidor    
    def clean(self): 
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        
        if first_name == last_name:
            msg = ValidationError('Primeiro nome igual ao segundo', code='invalid')

            self.add_error('first_name',msg)

        return super().clean()