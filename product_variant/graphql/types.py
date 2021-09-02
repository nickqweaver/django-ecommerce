from graphene import ObjectType, String, Int
from graphene_django import DjangoObjectType
from product_variant.models import WheelProductVariant


class WheelVariantType(DjangoObjectType):

    class Meta:
        # Reference the model you are accessing
        model = WheelProductVariant
        exclude = ('product_model',)
