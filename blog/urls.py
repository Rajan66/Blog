from django.contrib import admin
from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView,DeletePostView,AddCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-details'),
    # int:pk:- to reference the primary of the particular blog post
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='edit-post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete-post'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
]
