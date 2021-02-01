from django.urls import path
from .views import UserRegistrationView, UserDetailView, UserUpdateView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='register'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('profile/<int:pk>/edit', UserUpdateView.as_view(), name='editprofile'),
]
