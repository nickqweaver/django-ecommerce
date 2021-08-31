from django.db import models
from product.models import WheelProductModel
# Create your models here.


class BoltPatterns():
    RZR = 'RZR'
    CAN = 'CAN'
    BOLT_PATTERN_CHOICES = [
        (RZR, '14x136'),
        (CAN, '14x156'),
    ]

    def get_choices(self):
        return self.BOLT_PATTERN_CHOICES


class WheelSizes():
    XSMALL = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    XLARGE = 'XL'
    WHEEL_SIZE_CHOICES = [
        (XSMALL, '14x8'),
        (SMALL, '14x10'),
        (MEDIUM, '15x7'),
        (LARGE, '15x8'),
        (XLARGE, '15x10'),
    ]

    def get_choices(self):
        return self.WHEEL_SIZE_CHOICES


class WheelProductVariant(models.Model):
    size = models.CharField(
        max_length=2, choices=WheelSizes().get_choices(), default='M')
    bolt_pattern = models.CharField(
        max_length=3, choices=BoltPatterns().get_choices(), default='RZR')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_code = models.CharField(max_length=150)
    product_model = models.ForeignKey(
        WheelProductModel, on_delete=models.CASCADE, related_name='variants')
