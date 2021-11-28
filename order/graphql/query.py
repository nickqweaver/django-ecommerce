from graphene import List, Field, ObjectType, String, Int, ID, Field
from order.graphql.types import OrderItemQueryResponseType, OrderType, OrderItemResponseType
from order.models import Order
from product.models import BaseProduct

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
  
  return OrderType(order_items=parsed_order_items, status=order.status, id=order.id)


class OrderQuery(ObjectType):
    ## TODO Paginate Results
    get_all_user_orders = List(OrderType)
    get_order_by_id = Field(OrderType, id=ID())

    def resolve_get_all_user_orders(root, info):
        user = info.context.user
        orders = user.profile.orders.all()
        new_orders = []

        for order in orders:
          new_orders.append(parse_order(order))

        return new_orders

    def resolve_get_order_by_id(root, info, id):
      order = info.context.user.profile.orders.get(pk=id)
      return parse_order(order)
    
