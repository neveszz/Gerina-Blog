from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name','name')
choice_list = []

for item in choices:
    choice_list.append(item)

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category','description', 'header_image','body')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Post Title'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Insert a description to the blog post'}),
            'body' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Insert the text'}),
            }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your name'}),
            'body' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Insert the Comment'}),
        }