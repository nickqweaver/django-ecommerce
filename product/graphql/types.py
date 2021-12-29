from graphene_django import DjangoObjectType
from graphene import List, String, ObjectType, Decimal, Union, Boolean, ID, NonNull, Field
from product.models import WheelProductModel, TireProductModel, BaseProduct
from product_variant.graphql.types import VariationOptionType, WheelVariantType, TireVariantType, AllVariantsType

class CloudinaryImageType(ObjectType):
    id = NonNull(String)
    format = String()
    type = String()
    url = NonNull(String)

    def resolve_id(self, _info):
        return self.public_id

class ProductType(DjangoObjectType):
    variants = List(NonNull(AllVariantsType))
    has_different_variant_pricing = NonNull(Boolean)
    lowest_variant_price = NonNull(Decimal)
    variation_options = List(NonNull(VariationOptionType))
    image = Field(NonNull(CloudinaryImageType))
    brand = NonNull(String)

    class Meta:
        model = BaseProduct
        exclude = ('tireproductmodel', 'wheelproductmodel')

    def resolve_variants(self, _info):
        return self.get_product_variants()

    def resolve_lowest_variant_price(self, _info):
        return self.get_lowest_variant_price()

    def resolve_has_different_variant_pricing(self, _info):
        return self.has_different_variant_pricing()

    def resolve_variation_options(self, _info):
        return self.get_variation_options()

    def resolve_image(self, _info):
        return self.image

    def resolve_brand(self, _info):
        return self.brand


class PaginatedProductsType(ObjectType):
    has_more = Boolean()
    results = List(NonNull(ProductType))

class PaginatedProductIdsType(ObjectType):
    has_more = Boolean()
    results = List(NonNull(ID))
