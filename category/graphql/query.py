from graphene import List, Field, ObjectType, String, Int
from .types import ProductType
from category.models import Category
from .types import CategoryType
from product.graphql.types import AllProductType, PaginatedProductsType
from utils.paginator import Paginator
from product.graphql.types import ProductType


class CategoryQuery(ObjectType):
    get_all_categories = List(CategoryType)
    get_products_from_category = List(AllProductType, category_name=String())
    get_paginated_products_from_category = Field(
        PaginatedProductsType, category_name=String(), offset=Int(), limit=Int())

    def resolve_get_all_categories(root, info):
        try:
            categories = Category.objects.all()
            return categories
        except:
            raise Exception("There are no cateogries")

    def resolve_get_products_from_category(root, info, category_name):
        try:
            products = Category.objects.get(
                name__iexact=category_name).products.all().select_subclasses()
            return products
        except:
            raise Exception("There are no products with that category name")

    def resolve_get_paginated_products_from_category(root, info, category_name, offset, limit):
        products = Category.objects.get(name__iexact=category_name).products
        paginator = Paginator(products, True)
        return paginator.get_objects(offset, limit)
