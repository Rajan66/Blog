from django.urls import path
from .views import admin_login
from django.contrib import admin


urlpatterns = [
    path('', admin_login, name="admin_login")
]
