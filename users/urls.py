from django.urls import path
from .views import UserRegisterView


urlpatterns = [
    path('register/',UserRegisterView.as_view(), name='register'),
    # no need to make login url because the django.contrib.auth.urls automatically provides us with the login url.
]
