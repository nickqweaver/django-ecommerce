from django.db import models
from django.db.models.fields.related import ManyToManyField
from product.models import BaseProduct
from customer.models import Profile
class Order(models.Model):
    PENDING = 'PND'
    SHIPPED = 'SHP'
    FUFILLED = 'FUF'

    STATUS_CHOICES = (
      (PENDING, 'pending'),
      (SHIPPED, 'shipped'),
      (FUFILLED, 'fufilled'),
    )

    status = models.CharField(choices=STATUS_CHOICES, default=PENDING, max_length=3)
    profile = models.ForeignKey(Profile, related_name='orders', on_delete=models.CASCADE)

    def get_total_price(self):
      total = 0.00
      for order_item in self.order_items:
        product_id = order_item.product_id
        product_code = order_item.product_code
        unit_price = BaseProduct.objects.select_subclasses().get(pk=product_id).variants.get(product_code=product_code).unit_price

        total += unit_price
      return total

    def get_total_quantity(self):
      quantity = 0
      for order_item in self.order_items:
        quantity += order_item.quantity

      return quantity

    def __str__(self):
      return f'Order - {self.id}'

      
class OrderItem(models.Model):
  product_id = models.CharField(max_length=150, default='')
  variant_id = models.CharField(max_length=150, default='')
  quantity = models.IntegerField(default=0)
  total_price = models.DecimalField(editable=False, max_digits=10, decimal_places=2, default=0.00)
  order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)

  def check_stock(self, variation):
    if variation == None:
      return False
    has_stock = self.quantity <= variation.stock

    return has_stock
  
  def __str__(self):
    return f'{self.order.id}#{self.variant_id}'