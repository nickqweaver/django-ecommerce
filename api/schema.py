from graphene_django.converter import convert_django_field
from cloudinary.models import CloudinaryField
from graphene import String
from graphene_django import DjangoObjectType
import graphene

## CMD+SHIFT+P save w/o formatting for now, conversion registration needs to happen vefore imports
@convert_django_field.register(CloudinaryField)
def convert_cloudinary_to_string(field, registry=None):
    return field


from product.graphql.query import ProductQuery
from category.graphql.query import CategoryQuery


class Query(CategoryQuery, ProductQuery):
    pass


schema = graphene.Schema(Query)
