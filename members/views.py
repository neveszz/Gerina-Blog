from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from blogapp.models import Post, Profile
from .forms import ProfileForm, SignUpForm,EditProfileForm
# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm   
    template_name = 'members/register.html'
    success_url = reverse_lazy('login')
    
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm   
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        
        user_posts = Post.objects.filter(author=page_user.user)
        context['user_posts'] = user_posts
        
        return context
    
    
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio','profile_pic','website_url', 'instagram_url', 'linkedin_url']
    success_url = reverse_lazy('home')
    
class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/create_user_profile_page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)