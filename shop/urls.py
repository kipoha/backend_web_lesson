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
from product.views import products_view, main_view, category_view, detail_product_view, create_category, create_product, create_review
from user.views import reg_view, confirm_view, login_view, profile_view,logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', hello),
    # path('current_date/', current_date),
    # path('goodby/', goodby),
    path('', main_view, name='main_view'),
    path("categories/<int:category_id>/products/", products_view),
    path("categories/", category_view),
    path("categories/<int:category_id>/products/<int:product_id>/", detail_product_view),
    path("categories/create/", create_category),
    path("products/create/", create_product),
    path("categories/<int:category_id>/products/<int:product_id>/review/", create_review),
    path('register/', reg_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('profile/', profile_view, name='profile_view'),
    path('logout/', logout_view, name='logout_view'),
    path('confirm/', confirm_view, name='confirm_view'),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
