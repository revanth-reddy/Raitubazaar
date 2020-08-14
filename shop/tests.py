from django.test import TestCase
from .models import Category, Product
from django.utils import timezone


class CategoryTest(TestCase):

    def create_category(self, name="test category", slug="yes, this is only a test"):
        return Category.objects.create(name=name, slug=slug, created_at=timezone.now(), updated_at=timezone.now())

    def test_category_creation(self):
        w = self.create_category()
        self.assertTrue(isinstance(w, Category))
        self.assertEqual(w.__str__(), w.name)

class ProductTest(TestCase):
    
    def test_product_creation(self):
        c = Category.objects.create( name="test category", slug="yes, this is only a test", created_at=timezone.now(), updated_at=timezone.now())
        p = Product.objects.create(name="test product", slug="yes, this is only a test", category=Category.objects.get(name="test category"), description="test product description", price="100", available=True, stock=50, created_at=timezone.now(),updated_at=timezone.now())
        self.assertTrue(isinstance(c, Category))
        self.assertEqual(c.__str__(), c.name)
        self.assertTrue(isinstance(p, Product))
        self.assertEqual(p.__str__(), p.name)