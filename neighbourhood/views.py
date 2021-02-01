from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from django.shortcuts import redirect
from .models import Neighbourhood, Business

# Create your views here.


class NeighbourhoodDetailView(LoginRequiredMixin,DetailView):
    model = Neighbourhood
    template_name = 'neighbourhood.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs): # new
        return super().dispatch(request, *args, **kwargs)

class NeighbourhoodListView(LoginRequiredMixin,ListView):
    model = Neighbourhood
    template_name = 'neighbourhood_list.html'
    login_url = 'login'
