from graphene import List, Field, ObjectType
from .types import ProductType
from product.models import Product

class ProductQuery(ObjectType):
    get_all_products = List(ProductType)

    def resolve_get_all_products(root, info):
        return Product.objects.all()
