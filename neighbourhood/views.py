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
        return redirect('neighbourhood',pk=community_id)
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

# def search_results(request):
    # search_term = request.GET.get('search_term')
    # hood = request.GET.get('hood')
    # # print(search_results, hood)

    # businesses = Business.search_business(search_term,hood)
    # if businesses:
    #     return render(request,'neighbourhood.html', context={'object_list':businesses})
    # else:
    #     return render(request,'neighbourhood.html')
def search_results(request):
    if request.method == "GET":
        search_term = request.GET.get("search")
        businesses = Business.search_business(search_term)
        message = "{}".format(search_term)

        return render(request, "search.html", context={"message":message,
                                                                "businesses":businesses})
    message = "You haven't searched for any term"
    return render(request, "search.html", context={"message":message})

class CreateBusinessView(LoginRequiredMixin,CreateView):
    model = Business
    template_name = 'business_create.html'
    fields = ('image','name','location','description','category')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.neighbourhood = self.request.user.neighbourhood
        return super().form_valid(form)

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context
