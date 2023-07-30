from django.test import TestCase, Client
from django.urls import reverse


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class PageNotFoundViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_page_not_found_view(self):
        response = self.client.get('non_existing_url')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
