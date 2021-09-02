from graphene import List, Field, ObjectType, ID, Union, Decimal, Int
from .types import ProductType
from product.models import BaseProduct
from .types import AllProductType, PaginatedProductsType
from utils.paginator import Paginator


class ProductQuery(ObjectType):
    get_all_products = List(AllProductType)
    get_product_by_id = Field(AllProductType, id=ID())
    get_all_paginated_products = Field(
        PaginatedProductsType, offset=Int(), limit=Int())

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
        paginator = Paginator(BaseProduct, True)
        return paginator.get_objects(offset, limit)
