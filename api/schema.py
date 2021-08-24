import graphene
from graphene_django import DjangoObjectType
from product.query import ProductQuery


class Query(ProductQuery):
    pass


schema = graphene.Schema(query=Query)
