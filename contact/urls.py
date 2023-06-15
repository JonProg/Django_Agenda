from contact import views
from django.urls import path

app_name = 'contact'

urlpatterns = [
    path('', views.index , name='index'),
    path('search/', views.search , name='search'),

    #contact (CRUD)
    path('contact/<int:contact_id>/', views.contact , name='contact'),
    path('contact/<int:contact_id>/update/', views.update , name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    path('contact/create/', views.create , name='create'),
]