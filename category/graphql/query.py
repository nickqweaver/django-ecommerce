from graphene import List, Field, ObjectType, String
from .types import ProductType
from category.models import Category
from .types import CategoryType
from product.graphql.types import ProductType

class CategoryQuery(ObjectType):
    get_all_category_names = List(String)
    get_all_categories = List(CategoryType)
    get_products_from_category = List(ProductType, category_name=String())

    def resolve_get_all_category_names(root, info):
      try:
        category_names = Category.objects.all().values_list('name', flat=True)
        return category_names
      except:
        raise Exception("There are no categories")

    def resolve_get_all_categories(root, info):
      try:
        categories = Category.objects.all()
        return categories
      except:
        raise Exception("There are no cateogries")

    def resolve_get_products_from_category(root, info, category_name):
      try:
        products = Category.objects.get(name__iexact=category_name).products.all()
        return products
      except:
        raise Exception("There are no products with that category name")