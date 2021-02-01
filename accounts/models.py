from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from neighbourhood.models import Neighbourhood

# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='user_avatars', default='default.jpg')
    bio = models.TextField(blank=True, default='')
    neighbourhood = models.ForeignKey(Neighbourhood, related_name='residents', blank=True, null=True, on_delete=models.SET_NULL)


    def get_absolute_url(self):
        return reverse('profile', args=[self.id])
