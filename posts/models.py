from django.db import models
from neighbourhood.models import Neighbourhood
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.


class Tags(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tags, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('profile', args=[self.author.id])
