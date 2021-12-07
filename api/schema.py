from graphene_django.converter import convert_django_field
from cloudinary.models import CloudinaryField

## CMD+SHIFT+P save w/o formatting for now, conversion registration needs to happen vefore imports
@convert_django_field.register(CloudinaryField)
def convert_cloudinary_to_string(field, registry=None):
    return field

from graphene import String
from graphene_django import DjangoObjectType
import graphene
from order.graphql.mutation import OrderMutations
from order.graphql.query import OrderQuery
from customer.graphql.mutation import CustomerMutations
from customer.graphql.query import CustomerQuery


from product.graphql.query import ProductQuery
from category.graphql.query import CategoryQuery
from product_variant.graphql.query import VariantQuery

class Query(CategoryQuery, ProductQuery, VariantQuery, OrderQuery, CustomerQuery):
    pass

class Mutation(OrderMutations, CustomerMutations):
    pass

schema = graphene.Schema(Query, mutation=Mutation)
