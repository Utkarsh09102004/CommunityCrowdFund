from django.urls import path
from . import views

from django.urls import path
from .views import register, registration_success

urlpatterns = [
    path('register/', register, name='register'),
    path('registration_success/', registration_success, name='registration_success'),
]
