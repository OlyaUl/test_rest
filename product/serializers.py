# from rest_framewor
from rest_framework.serializers import ModelSerializer
from .models import Products, Category


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'product_category')