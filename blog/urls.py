from django.contrib import admin
from django.urls import path,include
from .views import HomeView,ArticleDetailView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-details'),
    # int:pk:- to reference the primary of the particular blog post
]
