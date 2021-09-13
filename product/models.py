from django.db import models
from category.models import Category
from brand.models import Brand
from model_utils.managers import InheritanceManager
from cloudinary.models import CloudinaryField


class BaseProduct(models.Model):
    name = models.CharField(max_length=150)
    image = CloudinaryField('image', default=None)
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, models.CASCADE,
                              related_name='products', default=None, blank=True)
    created_date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=50)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    objects = InheritanceManager()

    def __str__(self):
        return f'{self.name}'


def lowest_price(variants):
    min = variants[0].unit_price
    for variant in variants:
        if variant.unit_price < min:
            min = variant
    return min


def has_different_pricing(variants):
    compare = variants[0].unit_price
    has_different = False
    for variant in variants:
        if variant.unit_price != compare:
            has_different = True
    return has_different


class Common(models.Model):
    class Meta:
        abstract = True

    def get_lowest_variant_price(self):
        return lowest_price(self.variants.all())

    def has_different_variant_pricing(self):
        return has_different_pricing(self.variants.all())


class WheelProductModel(BaseProduct, Common):
    pass


class TireProductModel(BaseProduct, Common):
    pass
