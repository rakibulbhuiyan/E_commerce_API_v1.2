from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Brand,Category,Product
from .serializers import CategorySerializers,BrandSerializers,ProductSerializers
from rest_framework import viewsets
from .models import Brand


class CategoryView(viewsets.ViewSet):
    queryset=Category.objects.all()
    @extend_schema(responses=CategorySerializers)
    def list(self,request):
        serializer=CategorySerializers(self.queryset,many=True)
        return Response(serializer.data)


class BrandView(viewsets.ViewSet):
    queryset=Brand.objects.all()
    @extend_schema(responses=BrandSerializers)
    def list(self,request):
        serializer=BrandSerializers(self.queryset,many=True)
        return Response(serializer.data)


class ProductView(viewsets.ViewSet):
    queryset=Product.objects.all()
    @extend_schema(responses=ProductSerializers)
    def list(self,request):
        serializer=ProductSerializers(self.queryset,many=True)
        return Response(serializer.data)