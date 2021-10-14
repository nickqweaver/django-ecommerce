from django.db import models
from product.models import BaseProduct
## Start testing the order model with a Guest Checkout Option, this will not store any customer info on the Order
## Model. The customer would also obviously have no way to reference their order if none of their 
## Credentials were given

# The OrderItem can be staged on the frontend, but debating if it should be created in the DB
# Before an order is created, or if it should be done at the same time? (Probably when order is created)
# Or should OrderItems represent a users cart? 
# This could be weird with Guest Checkout, why would I save an order item in the db when a user is 
# not attached to it? 
class OrderItem(models.Model):
  ## Check stock method to ensure there are enough products before creating an order item
  ## Sum the price up based on quantity given
  product_id = models.CharField(max_length=150, default='')
  product_code = models.CharField(max_length=150, default='')
  quantity = models.IntegerField(default=0)
  total_price = models.DecimalField(editable=False, max_digits=10, decimal_places=2, default=0.00)

  def check_stock(self, variation):
    if variation == None:
      return False
    has_stock = self.quantity <= variation.stock

    return has_stock

  ## Check stock and calculate total_price before saving to DB
  # def save(self, *args, **kwargs):
  #   subclassed_product = BaseProduct.objects.select_subclasses().get(pk=self.product.id)
  #   variation = None

  #   try:
  #     variation = subclassed_product.variants.get(product_code=self.product_code)
  #   except:
  #     raise Exception("You cannot create an order with an invalid product code")
    
  #   has_stock = self.check_stock(variation)

  #   if has_stock:
  #     self.total_price = self.quantity * variation.unit_price
  #   else:
  #     raise Exception("")

  #   super().save(*args, **kwargs)

# The quantity/stock should not update on the variant until an order is created
# The order should not be created until payment is made
# This should work as we can throw an error if someone purchases the items a few seconds before soemone
# else

class Order(models.Model):
    PENDING = 'PND'
    SHIPPED = 'SHP'
    FUFILLED = 'FUF'

    STATUS_CHOICES = (
      (PENDING, 'pending'),
      (SHIPPED, 'shipped'),
      (FUFILLED, 'fufilled'),
    )

    order_items = models.ForeignKey(OrderItem, related_name='order_items', on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, default=PENDING, max_length=3)

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