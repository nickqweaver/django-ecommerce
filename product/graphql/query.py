from graphene import List, Field, ObjectType, ID, Union, Decimal, Int, String
from product.models import BaseProduct
from .types import ProductType, PaginatedProductsType
from utils.paginator import Paginator


class ProductQuery(ObjectType):
    get_all_products = List(ProductType)
    get_product_by_id = Field(ProductType, id=ID())
    get_all_paginated_products = Field(
        PaginatedProductsType, offset=Int(), limit=Int())
    get_product_by_slug = Field(ProductType, slug=String())

    def resolve_get_all_products(root, info):
        try:
            products = BaseProduct.objects.all().select_subclasses()
            return products
        except:
            raise Exception("There are no products")

    def resolve_get_product_by_id(root, info, id):
        try:
            product = BaseProduct.objects.select_subclasses().get(pk=id)
            return product
        except:
            raise Exception("There is no product with that ID")

    def resolve_get_all_paginated_products(root, info, offset, limit):
        paginator = Paginator(BaseProduct.objects, True)
        return paginator.get_objects(offset, limit)

    def resolve_get_product_by_slug(root, info, slug):
        try:
            product = BaseProduct.objects.select_subclasses().get(slug=slug)
            return product
        except:
            raise Exception("There is no product with that slug")
