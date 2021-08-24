from django.db import models
from product.models import Product
# Create your models here.

class BrandOption(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Option(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class OptionItem(models.Model):
    name = models.CharField(max_length=100)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.option.name} - {self.name}'


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    option_item = models.ForeignKey(
        OptionItem, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.option_item.name

class ProductBrandOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand_option = models.ForeignKey(
        BrandOption, on_delete=models.CASCADE, default=None)

