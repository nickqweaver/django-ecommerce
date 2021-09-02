from graphene import List, Field, ObjectType, ID, Union, Decimal
from .types import ProductType
from product.models import BaseProduct, WheelProductModel, TireProductModel
from product_variant.graphql.types import WheelVariantType
from graphene_django import DjangoObjectType


class WheelProductType(DjangoObjectType):
    lowest_variant_price = Decimal()
    variants = List(WheelVariantType)

    class Meta:
        model = WheelProductModel

    def resolve_lowest_variant_price(root, info):
        return root.get_lowest_variant_price()

    def resolve_variants(root, info):
        return root.variants.all()


class TireProductType(DjangoObjectType):
    lowest_variant_price = Decimal()

    class Meta:
        model = TireProductModel

    def resolve_lowest_variant_price(root, info):
        return root.get_lowest_variant_price()


class AllProductType(Union):

    class Meta:
        types = (WheelProductType, TireProductType)
        exclude = ('tireproductmodel', 'wheelproductmodel',)


class ProductQuery(ObjectType):
    get_all_products = List(AllProductType)
    get_product_by_id = Field(AllProductType, id=ID())

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
