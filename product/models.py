from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    image = models.ImageField(upload_to='media/product_imgs/%Y/%m/%d', null=True, default=None, blank=True)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='product'
    )
    
    def __str__(self):
        return self.product_name

class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user'
    )

    def __str__(self):
        return f'Review for {self.product.product_name}'

