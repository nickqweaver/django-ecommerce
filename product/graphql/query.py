from graphene import List, Field, ObjectType, ID, Int, String, NonNull
from product.models import BaseProduct
from .types import PaginatedProductsType, ProductType
from utils.paginator import Paginator


class ProductQuery(ObjectType):
    get_all_products = List(NonNull(ProductType))
    get_product_by_id = Field(ProductType, id=ID())
    get_all_paginated_products = Field(
        PaginatedProductsType, offset=Int(), limit=Int())
    get_product_by_slug = Field(ProductType, slug=String())
    get_base_prod = List(NonNull(ProductType))

    @staticmethod
    def resolve_get_all_products(_root, _info):
        try:
            products = BaseProduct.objects.all()
            return products
        except:
            raise Exception("There are no products")

    @staticmethod
    def resolve_get_product_by_id(_root, _info, id):
        try:
            product = BaseProduct.objects.get(pk=id)
            return product
        except:
            raise Exception("There is no product with that ID")

    @staticmethod
    def resolve_get_all_paginated_products(_root, _info, offset, limit):
        paginator = Paginator(BaseProduct.objects, False)
        return paginator.get_objects(offset, limit)

    @staticmethod
    def resolve_get_product_by_slug(_root, _info, slug):
        try:
            product = BaseProduct.objects.get(slug=slug)
            return product
        except:
            raise Exception("There is no product with that slug")

    @staticmethod
    def resolve_get_base_prod(_self, _info):
        return BaseProduct.objects.all()
