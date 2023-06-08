from django.db import models
from django.utils import timezone

class Contact(models.Model):
    firt_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateField(default=timezone.now) 
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.firt_name} {self.last_name}'
