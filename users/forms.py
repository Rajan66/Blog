from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile


# To make fields of user registration form
# this sets the fields in the database
# also sets the fields in the form that we use in the html template

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    
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


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio","profile_pic", "facebook_url", "instagram_url","twitter_url"]
        widgets = {
            'bio': forms.Textarea(attrs={'class':'form-control'}),
            # 'profile_pic': forms.Textarea(attrs={'class':'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class':'form-control'}),
        }
  
   