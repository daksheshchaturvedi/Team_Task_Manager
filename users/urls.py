# users/urls.py
from django.urls import path
from .views import user_login
from .views import register

urlpatterns = [
    path('users/login/', user_login, name='login'),
    path('users/register/', register, name='register'),
]