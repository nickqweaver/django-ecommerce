from graphene import List, Field, ObjectType, String, Int, ID, Field
from order.graphql.types import OrderFilterInputType, OrderItemQueryResponseType, OrderType
from order.models import Order
from product.models import BaseProduct
from graphql_jwt.decorators import login_required
from datetime import datetime

def parse_order(order):
  parsed_order_items = []
  for order_item in order.order_items.all():
    try:
      subclassed_product = BaseProduct.objects.select_subclasses().get(pk=order_item.product_id)
      variation = subclassed_product.variants.get(pk=order_item.variant_id)
      image = subclassed_product.image
      
      parsed_order_item = OrderItemQueryResponseType(product_variation=variation, image=image, product_name=subclassed_product.name)
      parsed_order_items.append(parsed_order_item)
    except:
      raise Exception("Could not retrieve order item details")
  
  return OrderType(order_items=parsed_order_items, status=order.status, id=order.id, totalPrice=order.get_total_price(), date_placed=order.date_placed)


class OrderQuery(ObjectType):
    ## TODO Paginate Results
    get_orders = List(OrderType, filter=OrderFilterInputType()) ## Can we add a filter option as an optional arg instead of queyr by ID?
    get_order_by_id = Field(OrderType, id=ID())
    
    @login_required
    def resolve_get_orders(root, info, filter):
        user = info.context.user
        orders = None

        new_orders = []

        if filter and filter.by:
          orders = user.profile.orders.all()
          if filter.by.ids:
            orders.filter(pk__in=filter.by.ids)
          if filter.by.date:
            ## This works but how do we chain them together dynamically?
            ## If we set to all first then none of the filters get applied
            orders = user.profile.orders.filter(date_placed__range=[filter.by.date.start, filter.by.date.end], pk__in=filter.by.ids)
        else:
          orders = user.profile.orders.all()
     
        for order in orders:
          new_orders.append(parse_order(order))

        return new_orders

    ## Deprecate this, use a filter in the above query instead so user will be limited to their own orders
    @login_required
    def resolve_get_order_by_id(root, info, id):
      order = info.context.user.profile.orders.get(pk=id)
      return parse_order(order)
    
