from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

# Create your tests here.

class TestPosts(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='test user',
         email="testuser@gmailcom", password='password')


    def test_is_instance(self):
        self.assertIsInstance(self.test_user, CustomUser)

    def test_str_method(self):
        self.assertEqual(f'{self.test_user}', 'test user')

    def test_user_registration_template_used(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'registration.html')

    def test_user_registration_url_exists_at_proper_location(self):
        resp = self.client.get('/users/registration/')
        self.assertEqual(resp.status_code,200)


    def test_login_required_mixin(self):
        response = self.client.get(reverse('editprofile', args=[self.test_user.id]))
        self.assertEqual(response.status_code,302)
