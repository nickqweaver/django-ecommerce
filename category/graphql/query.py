from graphene import List, Field, ObjectType, String, Int, ID
from category.models import Category
from .types import CategoryType
from product.graphql.types import ProductType, PaginatedProductIdsType
from utils.paginator import Paginator, PaginatedResults


class CategoryQuery(ObjectType):
    get_all_categories = List(CategoryType)
    get_product_ids_from_category = List(ID, category_name=String())
    get_paginated_product_ids_from_category = Field(
        PaginatedProductIdsType, category_name=String(), offset=Int(), limit=Int())

    def resolve_get_all_categories(root, info):
        try:
            categories = Category.objects.all()
            return categories
        except:
            raise Exception("There are no cateogries")

    def resolve_get_product_ids_from_category(root, info, category_name):
        category = Category.objects.get(name__iexact=category_name)
        return category.get_product_ids()

    def resolve_get_paginated_product_ids_from_category(root, info, category_name, offset, limit):
        products = Category.objects.get(
            name__iexact=category_name).products
        paginator = Paginator(products, True)
        results = paginator.get_objects(offset, limit).results
        product_ids = []

        for result in results:
            product_ids.append(result.id)

        return PaginatedResults(product_ids, paginator.has_more)
