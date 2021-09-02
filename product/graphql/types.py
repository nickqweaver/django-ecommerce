from graphene_django import DjangoObjectType
from graphene import Field, List, String, ObjectType, Decimal, Union, Boolean
from product.models import BaseProduct, WheelProductModel, TireProductModel
from product_variant.graphql.types import WheelVariantType, TireVariantType


class ProductType(DjangoObjectType):
    class Meta:
        # Reference the model you are accessing
        model = BaseProduct
        exclude = ('tireproductmodel', 'wheelproductmodel')

    def resolve_brand(root, info):
        return root.brand.name


class CommonProductFields(ObjectType):
    brand = String()
    lowest_variant_price = Decimal()
    has_different_variant_pricing = Boolean()

    def resolve_brand(root, info):
        return root.brand.name

    def resolve_lowest_variant_price(root, info):
        return root.get_lowest_variant_price()

    def resolve_has_different_variant_pricing(root, info):
        return root.has_different_variant_pricing()


class WheelProductType(DjangoObjectType, CommonProductFields):
    variants = List(WheelVariantType)

    class Meta:
        model = WheelProductModel

    def resolve_variants(root, info):
        return root.variants.all()


class TireProductType(DjangoObjectType, CommonProductFields):
    variants = List(TireVariantType)

    class Meta:
        model = TireProductModel

    def resolve_variants(root, info):
        return root.variants.all()


class AllProductType(Union):

    class Meta:
        types = (WheelProductType, TireProductType)
        exclude = ('tireproductmodel', 'wheelproductmodel',)


class PaginatedProductsType(ObjectType):
    has_more = Boolean()
    results = List(AllProductType)
