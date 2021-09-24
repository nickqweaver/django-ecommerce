from graphene import ObjectType, String, Union, NonNull, List
from graphene_django import DjangoObjectType
from product_variant.models import WheelProductVariant, TireProductVariant

class VariationOptionType(ObjectType):
    label = NonNull(String)
    options = List(NonNull(String))

class WheelVariantType(DjangoObjectType):
    class Meta:
        # Reference the model you are accessing
        model = WheelProductVariant
        exclude = ('product_model',)
        convert_choices_to_enum = False

    def resolve_variation_options(root, info):
        obj = {
            'label': "Fake",
            'options': ['ONE', 'TWO']
        }
        li = [obj]
        return li


class TireVariantType(DjangoObjectType):
    class Meta:
        # Reference the model you are accessing
        model = TireProductVariant
        exclude = ('product_model',)
        convert_choices_to_enum = False


class AllVariantsType(Union):
    class Meta:
        types = (WheelVariantType, TireVariantType)
