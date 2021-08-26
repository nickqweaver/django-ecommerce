from category.models import Category
from product.graphql.types import ProductType 
from graphene_django import DjangoObjectType
from graphene import List

class CategoryType(DjangoObjectType):
  products = List(ProductType)
  
  class Meta:
    model = Category

  def resolve_products(self, info):
    products = self.products.all()
    return products
