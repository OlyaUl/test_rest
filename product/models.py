from django.db import models
from datetime import datetime


class Category(models.Model):
    name = models.CharField(max_length=30)


class Products(models.Model):
    name = models.CharField(max_length=30)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
