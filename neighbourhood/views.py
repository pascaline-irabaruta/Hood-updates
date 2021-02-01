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

@login_required(login_url='login')
def join_neighbourhood(request, community_id):
    if(request.user.neighbourhood == None ):
        new_hood = Neighbourhood.objects.get(id=community_id)
        request.user.neighbourhood  = new_hood
        request.user.save()
        return redirect('neighbourhood',pk=1)
    else:
        # return render(request, 'neighbourhood_list.html')
         return redirect('neighbourhood_list')

@login_required(login_url='login')
def leave_neighbourhood(request, community_id):
    if request.method == 'GET':
        return render(request, 'neighbourhood_leave.html')
    else:
        request.user.neighbourhood = None
        request.user.save()
        return redirect('mainpage')
