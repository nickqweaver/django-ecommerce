from django.db import models
from product.models import WheelProductModel, TireProductModel
from .choices import WheelSizes, BoltPatterns, Sizes
# Create your models here.


class BaseVariant(models.Model):
    product_code = models.CharField(max_length=150, default='')
    stock = models.IntegerField(default=0)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        abstract = True


class WheelProductVariant(BaseVariant):
    SIZE_CHOICES = (
        ('14x8', '14x8'),
        ('14x10', '14x10'),
        ('15x7', '15x7'),
        ('15x8', '15x8'),
        ('15x10', '15x10'),
    )

    class BoltPattern(models.TextChoices):
        RZR = '14x136'
        CAN = '14x156'

    size = models.CharField(
        max_length=6, choices=SIZE_CHOICES, default='15x7')
    bolt_pattern = models.CharField(
        max_length=6, choices=BoltPattern.choices, default='RZR')
    finish = models.CharField(max_length=150, blank=True)
    product_model = models.ForeignKey(
        WheelProductModel, on_delete=models.CASCADE, related_name='variants')


class TireProductVariant(BaseVariant):
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
