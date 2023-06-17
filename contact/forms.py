from contact import models
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):

    picture = forms.ImageField(
        widget = forms.FileInput(
            attrs = {
                'accept':'image/*'
            }
        )
    )
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            'picture',
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


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )

    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name',
            'email', 'username', 'password1',
            'password2',
        )
    
    def clean_email(self):
        email = self.cleaned_data.get('email') #Peagndo o valor email

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code = 'invalid')
            )

        return email