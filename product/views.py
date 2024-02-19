from django.shortcuts import render
from django.http import HttpResponse
import datetime
from product.models import Product, Category, Review

# def hello(request):
#     return HttpResponse('Hello! Its my project')

# def current_date(request):
#     date = datetime.datetime.now()
#     text = date.strftime('%d.%m.%Y')
#     return HttpResponse(f'Current date: {text}')

# def goodby(request):
#     return HttpResponse('Goodby user!')


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def products_view(request, category_id):
    if request.method == 'GET':
        try:
            category = Category.objects.get(id=category_id)
            products = Product.objects.filter(category=category)
            return render(request, 'products/products.html', context={'products': products})
        except:
            return render(request, 'error/404.html')

def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'products/categories.html', context={'categories': categories})

def detail_product_view(request, category_id, product_id):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
            return render(request, 'products/detail_product.html', context={'product': product})
        except:
            return render(request, 'error/404.html')
            