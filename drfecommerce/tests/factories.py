import factory
from app.models import Product,Brand,Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Category
    name="test_cat"

    
class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Product
    name="test_Product"
    desc="test_desc"
    is_digital=True
    brand=factory.SubFactory(BrandFactory)
    category=factory.SubFactory(CategoryFactory)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Brand
    name="test_prod"
    