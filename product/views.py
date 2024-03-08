from django.db.models.base import Model as Model
from django.shortcuts import render, redirect
from product.models import Product, Category, Review
from product.forms import CategoryForm, ProductForm, ReviewForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy

class MainView(View):
    def get(self, request):
        if request.method == 'GET':
            return render(request, 'index.html')

class ProductsView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 3
    login_url = '/login/' 

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs['category_id']
        category = Category.objects.get(id=category_id)
        queryset = queryset.filter(category=category).exclude(author=self.request.user)

        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(product_name__icontains=search) |
                Q(description__icontains=search)
            )

        sort = self.request.GET.get('sort')
        if sort == 'created':
            order = self.request.GET.get('order')
            if order == 'asc':
                queryset = queryset.order_by('created')
            else:
                queryset = queryset.order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = range(1, context['paginator'].num_pages + 1)
        return context

class CategoryView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'products/categories.html'
    context_object_name = 'categories'
    login_url = '/login/'

class DetailProduct(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/detail_product.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'
    login_url = '/login/' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewForm()
        return context

class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'products/detail_product.html'
    login_url = '/login/' 

    def form_valid(self, form):
        product_id = self.kwargs['product_id']
        form.instance.product_id = product_id
        form.instance.user = self.request.user
        form = super().form_valid(form)
        return form

    def get_success_url(self):
        category_id = self.kwargs['category_id']
        product_id = self.kwargs['product_id']
        return reverse('detail_product_view', kwargs={'category_id': category_id, 'product_id': product_id})

class CreateCategory(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'create/create.html'
    success_url = '/categories/'
    login_url = '/login/'

class CreateProduct(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create/create.html'
    login_url = '/login/'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        category_id = self.object.category.id
        return f'/categories/{category_id}/products/'

class UpdateProduct(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/update_product.html'
    pk_url_kwarg = 'product_id'
    login_url = '/login/'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user != obj.author:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        category_id = self.kwargs['category_id']
        return reverse_lazy('detail_product_view', kwargs={'category_id': category_id, 'product_id': self.object.id})
