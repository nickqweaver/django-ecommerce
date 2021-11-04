from category.models import Category
from graphene_django import DjangoObjectType
from graphene import List, ID


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        exclude = ('products',)
