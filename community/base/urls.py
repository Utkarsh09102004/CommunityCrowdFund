from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('registration_success/', registration_success, name='registration_success'),
    path('login/', login_view, name='login'),
]
