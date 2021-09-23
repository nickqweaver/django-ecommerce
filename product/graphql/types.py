from graphene_django import DjangoObjectType
from graphene import Field, List, String, ObjectType, Decimal, Union, Boolean, ID, Date, NonNull
from product.models import BaseProduct, WheelProductModel, TireProductModel
from product_variant.graphql.types import WheelVariantType, TireVariantType, AllVariantsType
from category.graphql.types import CategoryType


class BaseProductType(DjangoObjectType):
    class Meta:
        # Reference the model you are accessing
        model = BaseProduct
        exclude = ('tireproductmodel', 'wheelproductmodel')

    def resolve_brand(root, info):
        return root.brand.name


class CommonProductFields(ObjectType):
    brand = NonNull(String)
    lowest_variant_price = NonNull(Decimal)
    has_different_variant_pricing = NonNull(Boolean)

    def resolve_brand(root, info):
        return root.brand.name

    def resolve_lowest_variant_price(root, info):
        return root.get_lowest_variant_price()

    def resolve_has_different_variant_pricing(root, info):
        return root.has_different_variant_pricing()


class CloudinaryImageType(ObjectType):
    id = NonNull(String)
    format = String()
    type = String()
    url = NonNull(String)

    def resolve_id(root, info):
        return root.public_id

    def resolve_format(root, info):
        return root.format

    def resolve_type(root, info):
        return root.type

    def resolve_url(root, info):
        return root.url


class ProductType(ObjectType):
    name = NonNull(String)
    id = NonNull(ID)
    image = Field(NonNull(CloudinaryImageType))
    description = NonNull(String)
    category = Field(NonNull(CategoryType))
    created_date = NonNull(Date)
    slug = NonNull(String)
    weight = NonNull(Decimal)
    variants = NonNull(List(NonNull(AllVariantsType)))
    brand = NonNull(String)
    lowest_variant_price = NonNull(Decimal)
    has_different_variant_pricing = NonNull(Boolean)

    def resolve_name(root, info):
        return root.name

    def resolve_id(root, info):
        return root.id

    def resolve_description(root, info):
        return root.description

    def resolve_category(root, info):
        return root.category

    def resolve_created_date(root, info):
        return root.created_date

    def resolve_slug(root, info):
        return root.slug

    def resolve_weight(root, info):
        return root.weight

    def resolve_variants(root, info):
        return root.variants.all()

    def resolve_brand(root, info):
        return root.brand.name

    def resolve_lowest_variant_price(root, info):
        return root.get_lowest_variant_price()

    def resolve_has_different_variant_pricing(root, info):
        return root.has_different_variant_pricing()

    def resolve_image(root, info):
        return root.image


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
    results = List(NonNull(ProductType))


class PaginatedProductIdsType(ObjectType):
    has_more = Boolean()
    results = List(NonNull(ID))
