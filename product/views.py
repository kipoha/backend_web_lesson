from django.shortcuts import render
from django.http import HttpResponse
import datetime
from product.models import Product

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

def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        for pr in products:
            ...
        return render(request, 'products/products.html', context={'products': products})