from graphene_django import DjangoObjectType
from graphene import Field, List, String, ObjectType, Int
from product.models import BaseProduct


class ProductType(DjangoObjectType):
    lowest_variant_price = Int()

    class Meta:
        # Reference the model you are accessing
        model = BaseProduct
        exclude = ('tireproductmodel', 'wheelproductmodel')

    def resolve_lowest_variant_price(root, info):
        return 10
