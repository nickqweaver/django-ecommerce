from graphene import List, Field, ObjectType, ID
from .types import ProductType
from product.models import Product

class ProductQuery(ObjectType):
    get_all_products = List(ProductType)
    get_product_by_id = Field(ProductType, id=ID())

    def resolve_get_all_products(root, info):
        try:
            products = Product.objects.all()
            return products
        except:
            raise Exception("There are no products")

    def resolve_get_product_by_id(root, info, id):
        try:
            product = Product.objects.get(pk=id)
            return product
        except:
            raise Exception("There is no product with that ID")
