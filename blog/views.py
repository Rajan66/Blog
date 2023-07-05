from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, User
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


# Class based views queries the database for us
# In functional view however we need to do it by ourselves
class HomeView(ListView):
    # ListView to view all the blog posts in the database
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    # does order by hour only by a whole day..
    # ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu

        return context


class ArticleDetailView(DetailView):
    # DetailView to view a single blog post
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)
        context['category_menu'] = category_menu

        return context


class AddPostView(CreateView):
    # CreateView to create a new blog post
    model = Post
    Post.author_id = User.id
    template_name = 'add_post.html'
    form_class = PostForm
    # fields = '__all__'
    # fields = ['title','title_tag','body']
    # to put all the fields from the post model, we use __all__


class AddCategoryView(CreateView):
    # CreateView to create a new blog post
    model = Category
    template_name = 'add_category.html'
    fields = ['name']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(
            *args, **kwargs)
        context['category_menu'] = category_menu

        return context


class UpdatePostView(UpdateView):
    # UpdateView to update fields in the blog post
    model = Post
    template_name = 'edit_post.html'
    form_class = EditForm

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu

        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context['category_menu'] = category_menu

        return context


# this is a functional view rather than a class based view
# this is useful here because we can pass the request and the category as paramter
# category meaning sports, entertainment, music or other categories that we have stored in the database
def CategoryView(request, cat):
    # This filters all the post of the specific category ie. cat (which ever is passed in the url)
    # Post meaning the Post table(model)
    post_category = Post.objects.filter(category=cat.replace('-', ' '))
    # title() function makes the first letter uppercase
    context = {'cat': cat.title().replace('-', ' '),
               'post_category': post_category}
    return render(request, 'categories.html', context)


def CategoryListView(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return render(request, 'category_list.html', context)


# get this object or return a 404 error if it doesn't exist
# after we press like we get the post's id then we pass that into this
# this says to look that post's id in the blog_post table
# and assign it to the post variable and we save it to the table
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    # request.user so that we can identify who liked the post
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        post.like_count -= 1
        result = post.like_count
        post.save()
    else:
        post.likes.add(request.user)
        post.like_count += 1
        result = post.like_count
        post.save()
    return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))
