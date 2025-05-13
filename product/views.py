from drf_spectacular.utils import extend_schema

from .serializer import BrandSerializer, ProductSerializer, CategorySerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from product.models import Brand, Product, Category


class BrandsView(viewsets.ViewSet):
    queryset = Brand.objects.all()

    @extend_schema(responses={200: BrandSerializer})
    def list(self, request):
        serializer_date=BrandSerializer(self.queryset, many=True)
        return Response(serializer_date.data)

class ProductView(viewsets.ViewSet):
    queryset = Product.objects.all()

    @extend_schema(responses={200: ProductSerializer})
    def list(self, request):
        serializer_date = ProductSerializer(self.queryset, many=True)
        return Response(serializer_date.data)

class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.all()

    @extend_schema(responses={200: CategorySerializer})
    def list(self, request):
        serializer_date = CategorySerializer(self.queryset, many=True)
        return Response(serializer_date.data)