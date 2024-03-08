"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product.views import MainView, CategoryView, DetailProduct, CreateCategory, CreateProduct, CreateReviewView, UpdateProduct, ProductsView
from user.views import reg_view, confirm_view, login_view, profile_view, logout_view, update_profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path("categories/<int:category_id>/products/", ProductsView.as_view()),
    path("categories/", CategoryView.as_view(), name='category_view'),
    path("categories/<int:category_id>/products/<int:product_id>/", DetailProduct.as_view(), name='detail_product_view'),
    path("categories/create/", CreateCategory.as_view()),
    path("products/create/", CreateProduct.as_view(), name='create_product'),
    path("categories/<int:category_id>/products/<int:product_id>/review/", CreateReviewView.as_view()),
    path('register/', reg_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('profile/', profile_view, name='profile_view'),
    path('logout/', logout_view, name='logout_view'),
    path('confirm/', confirm_view, name='confirm_view'),
    path("categories/<int:category_id>/products/<int:product_id>/update/", UpdateProduct.as_view(), name='update_product_view'),
    path('profile/update/', update_profile, name='profile_update'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
