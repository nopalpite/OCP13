from django.test import TestCase, Client
from django.urls import reverse
from .models import Address, Letting


class AddressModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street="Main Street",
            city="New York",
            state="NY",
            zip_code=10001,
            country_iso_code="USA"
        )

    def test_address_str_method(self):
        self.assertEqual(str(self.address), "123 Main Street")


class LettingModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=456,
            street="Park Avenue",
            city="Los Angeles",
            state="CA",
            zip_code=90001,
            country_iso_code="USA"
        )
        self.letting = Letting.objects.create(
            title="Luxury Apartment",
            address=self.address
        )

    def test_letting_str_method(self):
        self.assertEqual(str(self.letting), "Luxury Apartment")


class LettingViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.address = Address.objects.create(
            number=789,
            street="Broadway",
            city="Chicago",
            state="IL",
            zip_code=60007,
            country_iso_code="USA"
        )
        self.letting = Letting.objects.create(
            title="Cozy Studio",
            address=self.address
        )

    def test_index_view(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cozy Studio")
        self.assertTemplateUsed(response, 'lettings/index.html')

    def test_letting_view(self):
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cozy Studio")
        self.assertContains(response, "789 Broadway")
        self.assertTemplateUsed(response, 'lettings/letting.html')
