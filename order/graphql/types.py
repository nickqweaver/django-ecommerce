import graphene
from graphene import String, ObjectType, Field
from graphene_django import DjangoObjectType
from order.models import Order, OrderItem
from product.graphql.types import CloudinaryImageType
from product_variant.graphql.types import AllVariantsType

class OrderItemInput(graphene.InputObjectType):
  product_id = graphene.String()
  variant_id = graphene.String()
  quantity = graphene.Int()


class OrderType(DjangoObjectType):

  class Meta:
    model = Order


class OrderItemType(DjangoObjectType):

  class Meta:
    model = OrderItem


class OrderItemResponseType(ObjectType):
  product_variation = AllVariantsType()
  status = String() # 'error' | 'success
  message = String()
  image = Field(CloudinaryImageType)


