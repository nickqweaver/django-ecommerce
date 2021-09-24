from django.db import models
from django.db.models import base
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
    try:
        min = variants[0].unit_price
        for variant in variants:
            if variant.unit_price < min:
                min = variant
        return min
    except:
        raise Exception(
            "You need to add variants to your products otherwise we can't calculate a price")


def has_different_pricing(variants):
    try:
        compare = variants[0].unit_price
        has_different = False
        for variant in variants:
            if variant.unit_price != compare:
                has_different = True
        return has_different
    except:
        raise Exception(
            "You need to add variants to your products otherwise we can't calculate a price")

def parse_variation_options(variants):
        variant_field_names = variants[0].get_base_variant_field_names()
        ## We only want the keys that are specific to the submodel variant,
        ## all of these exclusion keys are in all base variant model
        exclusion_keys = {'product_model', 'unit_price', 'stock', 'product_code', 'id'}
        options = {}
        ## Build up a new dict w/ same keys as variants (not exclusion keys) and set values to empty sets
        for field_name in variant_field_names:
            is_valid_key = field_name not in exclusion_keys
            if (is_valid_key):
                options.update({field_name: set()})
    
        ## Fill sets in with values that have the same keys to form one dict
        for variant in variants:
            variant_dict = variant.__dict__
            for key, value in variant_dict.items():
                if (key in options):
                    options[key].add(value)

        ## Normalizes data to return a Pascal cased key name for the label, and the options set mapped to an options key
        variation_options = []
        for key, value  in options.items():
            variation_option = {
                'label': key.replace("_", " ").title(),
                'options': value
            }
            variation_options.append(variation_option)

        return variation_options

        
        
class Common(models.Model):
    class Meta:
        abstract = True

    def get_lowest_variant_price(self):
        return lowest_price(self.variants.all())

    def has_different_variant_pricing(self):
        return has_different_pricing(self.variants.all())
    
    def get_variation_options(self):
        return parse_variation_options(self.variants.all())


class WheelProductModel(BaseProduct, Common):
    pass


class TireProductModel(BaseProduct, Common):
    pass
