from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Imports User that we created (admin) also other common users
# Create your models here.


class Post(models.Model):
    # form in django
    title = models.CharField(max_length=225)
    # title tag: Title at the top of the html page
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete -  deletes all the posts when the user account is deleted
    body = RichTextField(blank=True,null=True)
    snippet = models.CharField(max_length=255)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="uncategorized")
    # user can like many posts and a post can have many likes
    likes = models.ManyToManyField(User, related_name='like')
    like_count =models.BigIntegerField(default=0)
    # related name :- fk that associates the many things to each other 

    def __str__(self):
        # To view the title and author of the post in the admin area
        # There will be a list of posts so it will be much straightforward
        return self.title + ' | ' + str(self.author)
        # self.author is a Object so need to parse to String

    def get_absolute_url(self):
        # returns the page to the specified url after submitting the form
        # return reverse("article-details", args=(str(self.id)))
        return reverse("home")


# A new model for the category so that we can add, edit and remove categories
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")
