from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('about/', views.About, name='About'),
    path('contact/', views.Contact, name='Contact'),
    path('events/', views.Events, name='Events'),
    path('booking/', views.Booking, name='Booking')
]
