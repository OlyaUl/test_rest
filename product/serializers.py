# from rest_framewor
from rest_framework.serializers import ModelSerializer
from .models import Products, Category


# class ProductSerializerTest(data={"name": "n1"}):
#     product_serializer = ProductSerializer()
#     product_serializer.is_valid()



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'product_category')


class CategorySerializer(ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ('name', 'products', )
