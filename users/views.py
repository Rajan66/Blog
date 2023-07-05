from typing import Any, Optional
from django.db import models
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CreateUserForm,EditProfileForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.views import generic

# Create your views here.


# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')
@csrf_exempt
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'registration/login.html', context)



class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    
    # this function gets all the info of the user to the edit form page
    def get_object(self):
        return self.request.user
    
    
class PasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password-success')
    
    # this function gets all the info of the user to the edit form page
    
def password_success(request):
    context = {}
    return render(request, 'registration/password_success.html', context)