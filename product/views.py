from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
from .models import Products, Category
from .serializers import ProductSerializer, CategorySerializer


def index(request):
    return render(request, 'product/index.html', {})


class ProductView(ListAPIView, CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    model = Products


class ProductDetailView(RetrieveUpdateDestroyAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    model = Products


class CategoryView(ListAPIView, CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    model = Category


class CategoryDetailView(RetrieveUpdateDestroyAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    model = Category


'''class ProductCreateView(ListAPIView, CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    model = Products'''
