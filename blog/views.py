from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView

from .models import Post


# Create your views here.
# def home(request):
#     context = {}
#     return render(request, 'home.html', context)
class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    

class AddPostView(CreateView):
    model=Post
    template_name = 'add_post.html'
    fields = '__all__'    
    # to put all the fields from the post model, we use __all__
    