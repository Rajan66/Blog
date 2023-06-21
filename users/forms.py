from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# To make fields of user registration form
# this sets the fields in the database
# also sets the fields in the form that we use in the html template

class CreateUserForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name",
                  "email", "username", "password1", "password2")
