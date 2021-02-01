from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse

# Create your models here.


class Neighbourhood(models.Model):
    image = models.ImageField(upload_to='neighbourhood_avatars', default='dummy_neighbourhood.jpg')
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    police_hotline= ArrayField(models.CharField(max_length=13, blank=True),size=3, blank=True, null=True)
    hospital_hotline= ArrayField(models.CharField(max_length=13, blank=True),size=3, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
