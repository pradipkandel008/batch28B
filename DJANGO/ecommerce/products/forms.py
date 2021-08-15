from django import forms
from .models import Product
from django.forms import ModelForm


class PersonForm(forms.Form):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    dob = forms.DateField()
    phone = forms.IntegerField()
    address = forms.CharField(max_length=200)


class ProductForm(ModelForm):
    category = forms.CharField(max_length=200)
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['name', 'price', 'stock']


