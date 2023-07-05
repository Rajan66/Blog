from django.contrib import admin
from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, LikeView,CategoryListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-details'),
    # int:pk:- to reference the primary of the particular blog post
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='edit-post'),
    # /remove : just so that the url is different and does not cause any err; url name can be anything here
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete-post'),
    path('add_category/', AddCategoryView.as_view(), name='add-category'),
    # str as the category name isn't an int like in the prev urls..
    path('category/<str:cat>/', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),
    path('like/<int:pk>', LikeView, name="like"),
]
