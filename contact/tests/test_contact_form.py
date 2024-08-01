from django.test import TestCase
from django.contrib.auth.models import User

class TestContactForm(TestCase):



    def test_setUp_user(self):
        self.user = User.objects.create_user()

    def test_contact_form_post_valid(self):
        form_data = {

        }