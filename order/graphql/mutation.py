import graphene
from graphql import GraphQLError
from product.models import BaseProduct
from order.models import OrderItem
from graphene import ObjectType

class CreateOrderItem(graphene.Mutation):
    response = graphene.String()

    class Arguments:
        # The input arguments for this mutation
        product_code = graphene.String(required=True)
        product_id = graphene.ID(required=True)
        quantity = graphene.Int()
        
    def mutate(root, info, product_code, product_id, quantity):
      subclassed_product = BaseProduct.objects.select_subclasses().get(pk=product_id)
      variation = None

      try:
        variation = subclassed_product.variants.get(product_code=product_code)
        order_item = OrderItem(product_id=product_id, product_code=product_code, quantity=quantity)
        has_stock = order_item.check_stock(variation)
        
        if has_stock:
            total_price = quantity * variation.unit_price
            order_item.total_price = total_price
            order_item.save()
        else:
            raise GraphQLError('There are not enough products in stock')
      except:
          raise GraphQLError("You cannot create an order with an invalid product code")
        # Notice we return an instance of this mutation
      return CreateOrderItem(response="Submitted")

class OrderMutations(ObjectType):
  create_order_mutation = CreateOrderItem.Field()