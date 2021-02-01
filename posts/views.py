from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Post

# Create your views here.


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = ('title', 'body', 'tags')
    login_url = 'login'


    def form_valid(self, form): # new
        form.instance.author = self.request.user
        form.instance.neighbourhood = self.request.user.neighbourhood
        return super().form_valid(form)
