from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from contact.forms import ContactForm

class TestContactForm(TestCase):



    def setUp(self):
        self.user = User.objects.create_user(username='testUser', password='12345')
        self.client.login(username='testUser', password='12345')
    
    def test_login(self):
        response = self.client.get(reverse('contact:user_update'))
        self.assertEqual(response.status_code, 200)

    def test_contact_form_post_valid(self):
        form_data = {
            'first_name':'Jhon',
            'last_name':'Henry',
            'phone':'(83)40028922',
            'email':'jhonHenry@gmail.com',
            'description':'My name is Jhon Henry, I am from california',
            'category':'1',
            'picture':None
        }

        form = ContactForm(data=form_data)
        print(form.__str__())
        self.assertTrue(form.is_valid())