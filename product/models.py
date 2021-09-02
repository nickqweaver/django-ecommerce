from django.db import models
from category.models import Category
from brand.models import Brand
from model_utils.managers import InheritanceManager

'''
 Look into possibly lifting the lowestVariantPrice logic up to the base product model
 Then have a universal product type, no need to query separate fragments to display 
 The store in a grid, the only time we would need product specifics is when a product is clicked, 
 then the variants would have to utilize fragments to get specific key values
'''


class BaseProduct(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='product_images/')
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


class WheelProductModel(BaseProduct):

    def get_lowest_variant_price(self):
        return lowest_price(self.variants.all())

    def has_different_variant_pricing(self):
        return has_different_pricing(self.variants.all())

    pass


class TireProductModel(BaseProduct):

    def get_lowest_variant_price(self):
        return lowest_price(self.variants.all())

    def has_different_variant_pricing(self):
        return has_different_pricing(self.variants.all())

    pass
