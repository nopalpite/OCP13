from django.test import TestCase, Client
from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="Bob",
            password="password",
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='New York'
        )

    def test_profile_str_method(self):
        self.assertEqual(str(self.profile), "Bob")


class ProfileViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username="Bob",
            password="password",
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='New York'
        )

    def test_index_view(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bob")
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_profile_view(self):
        response = self.client.get(reverse('profiles:profile', args=[self.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "New York")
        self.assertTemplateUsed(response, 'profiles/profile.html')
