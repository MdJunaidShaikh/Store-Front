from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(name='Test Product', description='This is a test product', 
                               price=99.99, stock=100, available=True)

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_description_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_stock_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('stock').verbose_name
        self.assertEquals(field_label, 'stock')

    def test_available_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('available').verbose_name
        self.assertEquals(field_label, 'available')

    def test_str_method(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.name}'
        self.assertEquals(expected_object_name, str(product))