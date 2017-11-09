from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView

# Create your views here.
from .models import Products
from .serializers import ProductSerializer


def index(request):
    return render(request, 'product/index.html', {})


class ProductView(ListAPIView, CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    model = Products


'''class ProductCreateView(ListAPIView, CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    model = Products'''
