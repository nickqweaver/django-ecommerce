from graphene_django import DjangoObjectType
from graphene import Field, List, String, ObjectType, Decimal, Union, Boolean, ID, NonNull
from product.models import WheelProductModel, TireProductModel
from product_variant.graphql.types import VariationOptionType, WheelVariantType, TireVariantType

class CloudinaryImageType(ObjectType):
    public_id = NonNull(String)
    format = String()
    type = String()
    url = NonNull(String)

class CommonProductType(ObjectType):
    has_different_variant_pricing = NonNull(Boolean)
    lowest_variant_price = NonNull(Decimal)
    variation_options = List(NonNull(VariationOptionType))

    def resolve_lowest_variant_price(self, _info):
        return self.get_lowest_variant_price()

    def resolve_has_different_variant_pricing(self, _info):
        return self.has_different_variant_pricing()

    def resolve_variation_options(self, info):
        return self.get_variation_options()

class WheelProductType(DjangoObjectType, CommonProductType):
    variants = List(WheelVariantType)

    class Meta:
        model = WheelProductModel

    def resolve_variants(self, _info):
        return self.variants.all()

class TireProductType(DjangoObjectType, CommonProductType):
    variants = List(TireVariantType)

    class Meta:
        model = TireProductModel

    def resolve_variants(self, _info):
        return self.variants.all()

class AllProductType(Union):
    class Meta:
        types = (WheelProductType, TireProductType)
        exclude = ('tireproductmodel', 'wheelproductmodel',)

class PaginatedProductsType(ObjectType):
    has_more = Boolean()
    results = List(NonNull(AllProductType))

class PaginatedProductIdsType(ObjectType):
    has_more = Boolean()
    results = List(NonNull(ID))
