from typing import Any
from django import forms
from product.models import Category, Product, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

        labels = {
            'category_name': 'Имя категории',
            'description': 'Описание',
        }


    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['author']

        labels = {
            'product_name': 'Имя',
            'description': 'Описание',
            'image': 'Изображение',
        }

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']
        labels = {
            'text': 'Отзыв'
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }