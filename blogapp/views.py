from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from .models import Post, Category, Comment
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from .forms import AddPostForm, CommentForm

# Create your views here.

def home(request):
    posts_list = Post.objects.all().order_by('-post_date')
    return render(request, 'home.html', {'posts_list':posts_list})

def article_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'article_details.html', {'post':post, 'total_likes':post.total_likes})

class AddPostView(CreateView):
    form_class = AddPostForm
    model = Post
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def edit_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.title_tag = request.POST['title_tag']
        post.description = request.POST['description']
        post.body = request.POST['body']
        post.save()
        return redirect(reverse('home'))
    else:
        return render(request, 'edit_post.html', {'post':post})
    

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect(reverse('home'))
    else:
        return render(request, 'remove_post.html', {'post':post})
    
class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'
    success_url = reverse_lazy('home')
    
def categories(request):
    category_list = Category.objects.all()
    return render(request, 'categories.html', {'category_list':category_list})

def category_view(request,cats):
    category_list = Post.objects.filter(category=cats).order_by('-post_date')
    return render(request,'category_posts.html', {'category_list':category_list, 'cats':cats.title()})


def LikeView(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(reverse('article_details', args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article_details', kwargs={'pk': self.kwargs['pk']})