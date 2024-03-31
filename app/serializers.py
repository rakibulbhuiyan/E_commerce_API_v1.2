from rest_framework import serializers
from .models import Category,Product,Brand

class CategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields=['name']

class BrandSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Brand
        fields=['name']

class ProductSerializers(serializers.ModelSerializer):
    brand=BrandSerializers()
    category=CategorySerializers()
    class Meta:
        model=Product
        fields='__all__'        