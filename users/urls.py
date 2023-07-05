from django.urls import path
from .views import registerPage,loginPage,UserEditView


urlpatterns = [
    path('register/',registerPage, name='register'),
    path('login/',loginPage, name='login'),
    path('edit_profile/',UserEditView.as_view(), name='edit-profile'),
    # no need to make login url because the django.contrib.auth.urls automatically provides us with the login url.
]
