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

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

    def get_absolute_url(self):
        return reverse('home')

class Business(models.Model):
    FOOD = 1
    BEAUTY = 2
    SOCIAL = 3
    ENTERTAINMENT = 4
    HOUSING = 5

    BUSINESS_CATEGORIES = [
        (FOOD, 'Food and Beverages'),
        (BEAUTY, 'Beauty shops'),
        (SOCIAL,'Social Amentity'),
        (ENTERTAINMENT, 'Entertainment'),
        (HOUSING, 'Housing'),
    ]

    image = models.ImageField(upload_to='business_avatars', default='business.jpg')
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.PositiveSmallIntegerField(choices=BUSINESS_CATEGORIES)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='businesses')

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def get_absolute_url(self):
        return reverse('neighbourhood', args=[self.neighbourhood.id])

    @classmethod
    def search_business(cls,search_term):
        return cls.objects.filter(
            models.Q(name__icontains = search_term),
            models.Q(description__icontains =search_term)
            )
