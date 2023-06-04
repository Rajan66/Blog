from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from .models import Post
from django.urls import reverse_lazy


# Create your views here.
# def home(request):
#     context = {}
#     return render(request, 'home.html', context)
class HomeView(ListView):
    # ListView to view all the blog posts in the database
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    # DetailView to view a single blog post
    model = Post
    template_name = 'article_details.html'
    

class AddPostView(CreateView):
    # CreateView to create a new blog post
    model=Post
    template_name = 'add_post.html'
    fields = '__all__'
    # fields = ['title','title_tag','body']    
    # to put all the fields from the post model, we use __all__
    
    
class UpdatePostView(UpdateView):
    # UpdateView to update fields in the blog post
    model = Post
    template_name = 'edit_post.html'
    fields = ['title','title_tag','body']
    
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    