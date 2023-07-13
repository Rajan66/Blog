from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from blog.views import HomeView
from .forms import CreateUserForm, EditProfileForm, ChangePasswordForm, CreateProfileForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import PasswordChangeView

from django.views.generic import DetailView, UpdateView, CreateView
from blog.models import Category, Profile

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

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
            # cleaned_data: a dictionary which contains cleaned data only from the fields which have passed the validation tests.
            # it will be only available after is_valid
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        else:
            print('Error 404')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def loginPage(request):
    if request.method == "post":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('home')
    context = {}
    return render(request, 'registration/login.html', context)


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    # this function gets all the info of the user to the edit form page
    def get_object(self):
        return self.request.user


class PasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password-success')


def password_success(request):
    context = {}
    return render(request, 'registration/password_success.html', context)


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView,
                        self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'facebook_url',
              'instagram_url', 'twitter_url']

    success_url = reverse_lazy('home')


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'registration/create_profile_page.html'

    # send the user who accessed the page to the form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
