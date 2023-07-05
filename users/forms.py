from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


# To make fields of user registration form
# this sets the fields in the database
# also sets the fields in the form that we use in the html template

class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email",
                  "username", "password1", "password2"]



class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
   
    class Meta:
        model = get_user_model()
        fields = ["email","first_name", "last_name", "username"]
        
        
class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
   
    class Meta:
        model = get_user_model()
        fields = ["old_password","new_password1", "new_password2"]
