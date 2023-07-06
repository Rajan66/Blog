from django.urls import path
from .views import registerPage,loginPage,UserEditView,PasswordView,ShowProfilePageView,EditProfilePageView,CreateProfilePageView
from . import views

urlpatterns = [
    path('register/',registerPage, name='register'),
    path('login/',loginPage, name='login'),
    # no need to make login url because the django.contrib.auth.urls automatically provides us with the login url.
    path('edit_profile/',UserEditView.as_view(), name='edit-profile'),
    path('password/',PasswordView.as_view(), name='password'),
    path('password_success/',views.password_success, name='password-success'),  
    path('<int:pk>/profile', ShowProfilePageView.as_view(), name="show-profile"),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(), name="edit-profile-page"),
    path('create_profile_page/', CreateProfilePageView.as_view(), name="create-profile-page"),
]
