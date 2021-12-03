from graphene import List, Field, ObjectType, String, Int, ID, Field
from order.graphql.types import OrderFilterInputType, OrderItemQueryResponseType, OrderType
from order.models import Order
from product.models import BaseProduct
from graphql_jwt.decorators import login_required
from datetime import datetime
from django.db.models import Q

from utils.filter_aggregator import FilterAggregator

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
        import operator
        import functools

        user = info.context.user
        orders = None

        new_orders = []

        filters = FilterAggregator("AND")
     
        # Only add the filters that were specified 
        if filter and filter.by:
          if filter.by.ids:
             filters.add(Q(pk__in=filter.by.ids))
          if filter.by.date:
            filters.add(Q(date_placed__range=[filter.by.date.start, filter.by.date.end]))
          if filter.by.price.eq:
            filters.add(Q(total_price=filter.by.price.eq))

        # Using reduce to concat all the Q Objects together with & operator to enable multiple filters
        if filter:
          orders = user.profile.orders.filter(filters.get_aggregated_results())
        else:
          orders = user.profile.orders.all()
     
        for order in orders:
          new_orders.append(parse_order(order))

        return new_orders
