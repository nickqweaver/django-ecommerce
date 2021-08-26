import graphene
from graphene_django import DjangoObjectType
from product.graphql.query import ProductQuery
from category.graphql.query import CategoryQuery


class Query(ProductQuery, CategoryQuery):
    pass


schema = graphene.Schema(query=Query)
