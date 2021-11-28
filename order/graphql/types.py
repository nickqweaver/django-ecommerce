import graphene
from graphene import String, ObjectType, Field, List, ID
from graphene_django import DjangoObjectType
from order.models import Order, OrderItem
from product.graphql.types import CloudinaryImageType
from product_variant.graphql.types import AllVariantsType

class OrderItemInput(graphene.InputObjectType):
  product_id = graphene.String()
  variant_id = graphene.String()
  quantity = graphene.Int()

class OrderItemType(DjangoObjectType):
  class Meta:
    model = OrderItem
    exclude = ("order",)

class OrderItemQueryResponseType(ObjectType):
  product_variation = AllVariantsType()
  product_name = String()
  image = Field(CloudinaryImageType)

class OrderItemResponseType(OrderItemQueryResponseType):
  response = String() # 'error' | 'success
  message = String()

class OrderType(ObjectType):
  order_items = List(OrderItemQueryResponseType)
  id = ID()
  status = String()