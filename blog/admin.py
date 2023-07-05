from django.contrib import admin
from .models import Post, Category,Profile
# Register your models here.

# This makes the blog post entries accessible from the admin area
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)