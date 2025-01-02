from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import UserProfile, Pet, Forum, Post

# UserProfile Views
class UserProfileListView(ListView):
    model = UserProfile
    template_name = "userprofile_list.html"

class UserProfileDetailView(DetailView):
    model = UserProfile
    template_name = "userprofile_detail.html"

class UserProfileCreateView(CreateView):
    model = UserProfile
    fields = ['user', 'profile_picture', 'bio']
    template_name = "userprofile_form.html"
    success_url = reverse_lazy('userprofile_list')

class UserProfileUpdateView(UpdateView):
    model = UserProfile
    fields = ['user', 'profile_picture', 'bio']
    template_name = "userprofile_form.html"
    success_url = reverse_lazy('userprofile_list')

class UserProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = "userprofile_confirm_delete.html"
    success_url = reverse_lazy('userprofile_list')

# Pet Views
class PetListView(ListView):
    model = Pet
    template_name = "pet_list.html"

class PetDetailView(DetailView):
    model = Pet
    template_name = "pet_detail.html"

class PetCreateView(CreateView):
    model = Pet
    fields = ['owner', 'name', 'species', 'breed', 'age']
    template_name = "pet_form.html"
    success_url = reverse_lazy('pet_list')

class PetUpdateView(UpdateView):
    model = Pet
    fields = ['owner', 'name', 'species', 'breed', 'age']
    template_name = "pet_form.html"
    success_url = reverse_lazy('pet_list')

class PetDeleteView(DeleteView):
    model = Pet
    template_name = "pet_confirm_delete.html"
    success_url = reverse_lazy('pet_list')

# Forum Views
class ForumListView(ListView):
    model = Forum
    template_name = "forum_list.html"

class ForumDetailView(DetailView):
    model = Forum
    template_name = "forum_detail.html"

class ForumCreateView(CreateView):
    model = Forum
    fields = ['title', 'description']
    template_name = "forum_form.html"
    success_url = reverse_lazy('forum_list')

class ForumUpdateView(UpdateView):
    model = Forum
    fields = ['title', 'description']
    template_name = "forum_form.html"
    success_url = reverse_lazy('forum_list')

class ForumDeleteView(DeleteView):
    model = Forum
    template_name = "forum_confirm_delete.html"
    success_url = reverse_lazy('forum_list')

# Post Views
class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreateView(CreateView):
    model = Post
    fields = ['forum', 'author', 'title', 'content']
    template_name = "post_form.html"
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ['forum', 'author', 'title', 'content']
    template_name = "post_form.html"
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy('post_list')
name = 'app/post.html'