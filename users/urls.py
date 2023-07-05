from django.urls import path
from .views import registerPage,loginPage,UserEditView,PasswordView
from . import views

urlpatterns = [
    path('register/',registerPage, name='register'),
    path('login/',loginPage, name='login'),
    # no need to make login url because the django.contrib.auth.urls automatically provides us with the login url.
    path('edit_profile/',UserEditView.as_view(), name='edit-profile'),
    path('password/',PasswordView.as_view(), name='password'),
    path('password_success/',views.password_success, name='password-success'),

]
