from django.urls import path

from .views import user_contacts

urlpatterns = [
    path('', user_contacts, name='contact')
]