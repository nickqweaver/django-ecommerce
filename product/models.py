from django.db import models
from category.models import Category


class Product(models.Model):
    sku = models.CharField(max_length=20)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    thumbnail = models.ImageField(blank=True, upload_to='product_images/')
    created_date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.SmallIntegerField()

    def __str__(self):
        return f' {self.name} - {self.sku}'
