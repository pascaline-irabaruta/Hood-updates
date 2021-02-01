from django.urls import path
from .views import NeighbourhoodDetailView, NeighbourhoodListView, join_neighbourhood, leave_neighbourhood, CreateBusinessView, search_results,AboutView
# , search_results

urlpatterns = [
    path('<int:pk>/',NeighbourhoodDetailView.as_view(),name='neighbourhood'),
    path('all/', NeighbourhoodListView.as_view(), name='neighbourhood_list' ),
    path('join/<int:community_id>/',join_neighbourhood, name='join_neighbourhood' ),
    path('leave/<int:community_id>/',leave_neighbourhood, name='leave_neighbourhood' ),
    path('leave/<community_id == ''>/',leave_neighbourhood, name='leave_neighbourhood' ),
    path('business/create/',CreateBusinessView.as_view(), name='create_business' ),
    path('search/',search_results,name='search_results'),
    path("about-us/", AboutView.as_view(), name="about"),
]
