from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CreateUserForm
# Create your views here.


# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/register.html'
#     success_url = reverse_lazy('login')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'registration/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'registration/register.html', context)
