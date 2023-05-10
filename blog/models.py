from django.db import models
from django.contrib.auth.models import User
# Imports User that we created (admin) also other common users 
# Create your models here.

class Post(models.Model):
    # form in django
    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete -  deletes all the posts when the user account is deleted
    body = models.TextField()
    
    def __str__(self):
        # To view the title and author of the post in the admin area 
        # There will be a list of posts so it will be much straightforward
        return self.title + ' | ' + str(self.author)
        # self.author is a Object so need to parse to String 