from graphene import ObjectType, String, Int, Union
from graphene_django import DjangoObjectType
from product_variant.models import WheelProductVariant, TireProductVariant


class WheelVariantType(DjangoObjectType):
    class Meta:
        # Reference the model you are accessing
        model = WheelProductVariant
        exclude = ('product_model',)
        convert_choices_to_enum = False


class TireVariantType(DjangoObjectType):
    class Meta:
        # Reference the model you are accessing
        model = TireProductVariant
        exclude = ('product_model',)
        convert_choices_to_enum = False


class AllVariantsType(Union):
    class Meta:
        types = (WheelVariantType, TireVariantType)
