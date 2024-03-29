from django import forms
from .models import Post, Category, Comment

# to pull the category from the database
# name is required twice syntax stuff
categories = Category.objects.all().values_list('name', 'name')
categories_list = []

for item in categories:
    # neccesary to make a python list as categories is QuerySet object which is difficult to manipulate
    categories_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category',
                  'body', 'snippet', 'header_image')

        widgets = {
            # placeholder = categories: add to the attrs; to show the querySet and list of the categories
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'category': forms.Select(choices=categories_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category',
                  'body', 'snippet', 'header_image')

        widgets = {
            # placeholder = categories: add to the attrs; to show the querySet and list of the categories
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=categories_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'})
        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Write a comment...',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ('content',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }