from django.urls import path
from .views import registerPage,loginPage


urlpatterns = [
    path('register/',registerPage, name='register'),
    path('login/',loginPage, name='login'),
    # no need to make login url because the django.contrib.auth.urls automatically provides us with the login url.
]
