from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from product.models import Product, Category, Review
from product.forms import CategoryForm, ProductForm, ReviewForm

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
            products = Product.objects.filter(category=category).select_related('category')
            return render(request, 'products/products.html', context={'products': products})
        except Exception as e:
            print(e)
            return render(request, 'error/404.html')

def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'products/categories.html', context={'categories': categories})

def detail_product_view(request, category_id, product_id):
    if request.method == 'GET':
        try:
            form = ReviewForm()
            product = Product.objects.get(id=product_id)
            return render(request, 'products/detail_product.html', context={'product': product, 'form': form})
        except:
            return render(request, 'error/404.html')

def create_category(request):
    if request.method == 'GET':
        form = CategoryForm()
        return render(
            request=request,
            template_name='create/create.html',
            context={"form": form}
        )
    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if not form.is_valid():
            return render(
                request=request,
                template_name='create/create.html',
                context={"form": form}
        )
        form.save()
        return redirect('/categories/')

def create_product(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(
            request=request,
            template_name='create/create.html',
            context={"form": form}
        )
    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(
                request=request,
                template_name='create/create.html',
                context={"form": form}
        )
        form.save()
        category_id = form.cleaned_data['category'].id
        return redirect(f'/categories/{category_id}/products/')

def create_review(request, category_id, product_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if not form.is_valid():
            return render(
                request=request,
                template_name='products/detail_product.html',
                context={'form': form}
            )
        review = form.save(commit=False)
        review.product_id = product_id
        review.save()
        return redirect(f'/categories/{category_id}/products/{product_id}/')