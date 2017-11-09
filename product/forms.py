from django import forms
from .models import Products, Category


class ProductForm(forms.ModelForm):
    # name = forms.CharField(help_text="this is name")
    # name = forms.CharField(max_length=10)

    class Meta:
        model = Products
        fields = '__all__'