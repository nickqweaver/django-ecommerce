from django.db import models
from product.models import WheelProductModel, TireProductModel
from .choices import WheelSizes, BoltPatterns, Sizes
# Create your models here.


class WheelProductVariant(models.Model):
    size = models.CharField(
        max_length=2, choices=WheelSizes().get_choices(), default=Sizes.MEDIUM)
    bolt_pattern = models.CharField(
        max_length=3, choices=BoltPatterns().get_choices(), default='RZR')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_code = models.CharField(max_length=150)
    product_model = models.ForeignKey(
        WheelProductModel, on_delete=models.CASCADE, related_name='variants')


class TireProductVariant(models.Model):
    class Height(models.IntegerChoices):
        TWENTY_EIGHT = 28
        TWENTY_NINE = 29
        THIRTY = 30
        THIRTY_ONE = 31
        THIRTY_TWO = 32
        THIRTY_THREE = 33
        THIRTY_FOUR = 34
        THIRTY_FIVE = 35

    class Width(models.IntegerChoices):
        EIGHT = 8
        NINE = 9
        TEN = 10

    class RimCircumference(models.IntegerChoices):
        FOURTEEN = 14
        FIFTEEN = 15
        SIXTEEN = 16

    height = models.IntegerField(choices=Height.choices)
    width = models.IntegerField(choices=Width.choices)
    rim_circumference = models.IntegerField(choices=RimCircumference.choices)
    product_model = models.ForeignKey(
        TireProductModel, on_delete=models.CASCADE, related_name='variants')
