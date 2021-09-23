from django.db import models
from product.models import WheelProductModel, TireProductModel
# Create your models here.


class BaseVariant(models.Model):
    product_code = models.CharField(max_length=150, default='')
    stock = models.IntegerField(default=0)
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        abstract = True

    def __str__(self):
        return self.product_code


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
    product_model = models.ForeignKey(
        WheelProductModel, on_delete=models.CASCADE, related_name='variants')


class TireProductVariant(BaseVariant):
    WIDTH_CHOICES = (
        (8, 8),
        (9, 9),
        (10, 10)
    )

    HEIGHT_CHOICES = (
        (28, 28),
        (29, 29),
        (30, 30),
        (31, 31),
        (32, 32),
        (33, 33),
        (34, 34),
        (35, 35),
    )

    RIM_CIRCUMFERENCE_CHOICES = (
        (14, 14),
        (15, 15),
        (16, 16)
    )

    class RimCircumference(models.IntegerChoices):
        FOURTEEN = 14
        FIFTEEN = 15
        SIXTEEN = 16

    height = models.IntegerField(choices=HEIGHT_CHOICES)
    width = models.IntegerField(choices=WIDTH_CHOICES)
    rim_circumference = models.IntegerField(choices=RIM_CIRCUMFERENCE_CHOICES)
    product_model = models.ForeignKey(
        TireProductModel, on_delete=models.CASCADE, related_name='variants')
