from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import detail_route
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Products, Category
from .serializers import ProductSerializer, CategorySerializer


def index(request):
    return render(request, 'product/index.html', {})


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    model = Products

    def get_queryset(self):
        return Products.objects.all()

    @detail_route(url='custom')
    def custom(self):
        return HttpResponse('custom_response')


# class ProductView(ListAPIView, CreateAPIView):
#     serializer_class = ProductSerializer
#     # queryset = Products.objects.all()
#     model = Products
#
#     def get_queryset(self):
#         return Products.objects.all()
#
#
# class ProductDetailView(RetrieveUpdateDestroyAPIView, UpdateAPIView, DestroyAPIView):
#     serializer_class = ProductSerializer
#     # queryset = Products.objects.all()
#     model = Products
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#
#     def get_queryset(self):
#         return Products.objects.all()


class CategoryView(ListAPIView, CreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    model = Category


class CategoryDetailView(RetrieveUpdateDestroyAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    model = Category
