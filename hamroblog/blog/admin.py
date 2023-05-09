from django.contrib import admin
from .models import Post
# Register your models here.

# This makes the blog post entries accessible from the admin area
admin.site.register(Post)