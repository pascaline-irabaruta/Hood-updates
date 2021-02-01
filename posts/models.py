from django.db import models
from neighbourhood.models import Neighbourhood
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Tags(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
