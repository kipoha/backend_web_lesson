from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='product_imgs/%Y/%m/%d', null=True, default=None)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    