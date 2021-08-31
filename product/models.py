from django.db import models
from category.models import Category
from brand.models import Brand
from option.models import Option


class BaseProduct(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, models.CASCADE,
                              related_name='brands', default=None, blank=True)
    created_date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=50)
    weight = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f' {self.name} - SKU: {self.sku}'


class WheelProductModel(BaseProduct):
    pass
