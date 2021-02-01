from django.test import TestCase
from django.urls import reverse
from .models import Neighbourhood, Business

# Create your tests here.

class TestNeighbourhood(TestCase):
    def setUp(self):
        self.test_hood = Neighbourhood.objects.create(name="test_hood", image="default.jpg",
         location="earth", police_hotline=[7238], hospital_hotline=[73774])

    def test_is_instance(self):
        self.assertIsInstance(self.test_hood, Neighbourhood)

    def test_str_method(self):
        self.assertEqual(f'{self.test_hood}', 'test_hood')

    def test_business_list_template_used(self):
        response = self.client.get(reverse('neighbourhood_list'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'neighbourhood_list.html')

    def test_business_detail_template_used(self):
        response = self.client.get(reverse('neighbourhood', args=[self.test_hood.id]))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'neighbourhood.html')




class TestBusiness(TestCase):
    def setUp(self):
        self.test_hood = Neighbourhood.objects.create(name="test_hood", image="default.jpg",
         location="earth", police_hotline=[7238], hospital_hotline=[73774])

        self.test_biz = Business.objects.create(name="test_biz", image="default.jpg",
         location="test_hood", description="Hello world", category=1, neighbourhood=self.test_hood)

    def test_is_instance(self):
        self.assertIsInstance(self.test_biz, Business)

    def test_str_method(self):
        self.assertEqual(f'{self.test_biz}', 'test_biz')

    def test_business_create_template_used(self):
        response = self.client.get(reverse('create_business'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'business_create.html')

    
    def test_business_create_url_exists_at_proper_location(self):
        resp = self.client.get('/neighbourhoods/business/create/')
        self.assertEqual(resp.status_code,200)
