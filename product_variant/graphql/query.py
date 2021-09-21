from product_variant.graphql.types import AllVariantsType
from graphene import List, Field, ObjectType, ID, Union, Decimal, Int, String
from product.models import BaseProduct
class VariantQuery(ObjectType):
  get_variant_by_id = Field(AllVariantsType, product_id=ID(), variant_id=ID())

  def resolve_get_variant_by_id(root, info, product_id, variant_id):
      try:
        product = BaseProduct.objects.select_subclasses().get(pk=product_id)
        variant = product.variants.get(pk=variant_id)
        return variant
      except:
        raise Exception("There was a problem with searching product variants")
