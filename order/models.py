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
    pass
    ## UUID instead of basic django ID?
    ## order_items = FK to order_item model (One order can hold many order items)
    ## status = "pending" | "shipped" | "fufilled" etc...
    ## FK to customer
    
    ## Helper methods
    ## getTotal - get total price of all order_items combined
    ## Or do we calculate the total and save it on the model? Not sure exactly how to do this
    ## getQuantity - get total number of items in the order