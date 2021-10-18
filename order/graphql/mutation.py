import graphene
from graphql import GraphQLError
from product.models import BaseProduct
from order.models import OrderItem, Order
from graphene import ObjectType, String, List, NonNull
from order.graphql.types import OrderItemInput, OrderItemResponseType


def create_order_items(order, product_code, product_id, quantity):
  
  try:
    subclassed_product = BaseProduct.objects.select_subclasses().get(pk=product_id)
    variation = subclassed_product.variants.get(product_code=product_code)
    image = subclassed_product.image
    order_item = OrderItem(order=order, product_id=product_id, product_code=product_code, quantity=quantity)
    has_stock = order_item.check_stock(variation)
    
    if has_stock:
        total_price = quantity * variation.unit_price
        variation.stock = variation.stock - quantity
        variation.save()
        order_item.total_price = total_price
        order_item.save()
    else:
        return OrderItemResponseType(variation, "error", "There are not enough items in stock for this product. This item could not be added to the order", image)
  except Exception as e:
      return OrderItemResponseType(None, "error", f'There was a problem adding item with product_id of {product_id} and product_code of {product_code}. Exception thrown was {e}', None)

  return OrderItemResponseType(variation, "success", f'The item was successfully added to order {order.id}', image)


class CreateOrder(graphene.Mutation):
  status = graphene.String()
  message = graphene.String()
  id = graphene.ID()
  order_items = graphene.List(NonNull(OrderItemResponseType))

  class Arguments:
    order_items = graphene.List(OrderItemInput)

  def mutate(root, info, order_items):
    order = Order.objects.create()
    order_item_responses = []
    status = "success"
    id = None

    for order_item in order_items:
      order_item_responses.append(create_order_items(order=order, product_id=order_item.product_id, product_code=order_item.product_code, quantity=order_item.quantity))

    ## If there are no items to add to the order we just delete the order from the DB
    if (len(order.order_items.all()) == 0):
      status = "error"
      message = "There were no items in the order. Order was not created"
      order.delete()
    else:
      order.save()
      message = "Successfully created order"
      id = order.id

    return CreateOrder(status=status, message=message, id=id, order_items=order_item_responses)

class OrderMutations(ObjectType):
  create_order = CreateOrder.Field()