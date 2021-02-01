from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from .models import Tags,Post
from neighbourhood.models import Neighbourhood

# Create your tests here.

class TestPosts(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(username='test_user',
         email="test_user@test,com", password='password')

        self.test_tag = Tags.objects.create(name="test_tag")

        self.test_hood = Neighbourhood.objects.create(name="test_hood", image="default.jpg",
         location="earth", police_hotline=[7238], hospital_hotline=[73774])

        self.test_post = Post.objects.create(title="test_post", neighbourhood=self.test_hood, author=self.test_user )

    def test_is_instance(self):
        self.assertIsInstance(self.test_tag, Tags)

    def test_is_instance_post(self):
        self.assertIsInstance(self.test_post, Post)

    def test_str_method(self):
        self.assertEqual(f'{self.test_post}', 'test_post')

    def test_login_mixin_redirect(self):
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code,302)


    def test_post_create_template_used(self):
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'post_create.html')

    def test_post_create_url_exists_at_proper_location(self):
        resp = self.client.get('/posts/create/')
        self.assertEqual(resp.status_code,200)
