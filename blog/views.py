from django.shortcuts import render
from django.views.generic import ListView,DetailView


# Create your views here.
# def home(request):
#     context = {}
#     return render(request, 'home.html', context)
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
