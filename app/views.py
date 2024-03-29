from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Brand,Category,Product
from .serializers import CategorySerializers
from rest_framework import viewsets
from .models import Brand


class CategoryView(viewsets.ViewSet):
    queryset=Category.objects.all()

    def list(self,request):
        serializer=CategorySerializers(self.queryset,many=True)
        return Response(serializer.data)

