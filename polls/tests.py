from django.test import TestCase
from django.urls import reverse
from .views import index, hello

# Create your tests here.
class ViewsTestCase(TestCase):
  def test_index_view(self):
    response = self.client.get(reverse('index'))
    self.assertEquals(response.status_code, 200)
    self.assertContains(response, "Hello, world. This change will make the test fail")

  def test_hello_view(self):
    response = self.client.get(reverse('hello'))
    self.assertEquals(response.status_code, 200)
    self.assertContains(response, 'El arroz con leche sabe a pollo')
