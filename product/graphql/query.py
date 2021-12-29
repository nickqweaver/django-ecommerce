from graphene import List, Field, ObjectType, ID, Int, String, NonNull
from product.models import BaseProduct
from .types import PaginatedProductsType, AllProductType
from utils.paginator import Paginator


class ProductQuery(ObjectType):
    get_all_products = List(NonNull(AllProductType))
    get_product_by_id = Field(AllProductType, product_id=ID())
    get_all_paginated_products = Field(
        PaginatedProductsType, offset=Int(), limit=Int())
    get_product_by_slug = Field(AllProductType, slug=String())

    @staticmethod
    def resolve_get_all_products(_root, _info):
        try:
            products = BaseProduct.objects.all().select_subclasses()
            return products
        except:
            raise Exception("There are no products")

    @staticmethod
    def resolve_get_product_by_id(_root, _info, product_id):
        try:
            product = BaseProduct.objects.select_subclasses().get(pk=product_id)
            return product
        except:
            raise Exception("There is no product with that ID")

    @staticmethod
    def resolve_get_all_paginated_products(_root, _info, offset, limit):
        paginator = Paginator(BaseProduct.objects, True)
        return paginator.get_objects(offset, limit)

    @staticmethod
    def resolve_get_product_by_slug(_root, _info, slug):
        try:
            product = BaseProduct.objects.select_subclasses().get(slug=slug)
            return product
        except:
            raise Exception("There is no product with that slug")
