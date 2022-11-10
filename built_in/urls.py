from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views
from .views import user_login

urlpatterns = [
    path('second_login/', user_login, name = 'second_login'),
]