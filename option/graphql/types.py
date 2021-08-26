from graphene_django import DjangoObjectType
from option.models import ProductOption, Option
from graphene import Field

class OptionType(DjangoObjectType):

  class Meta:
    model = Option

## { optionName: String, options: [String]}
class ProductOptionType(DjangoObjectType):
    option_items = Field("option.graphql.types.OptionType")
    
    class Meta:
        # Reference the model you are accessing
        model = ProductOption
        exclude = ("product",)


    def resolve_product_option(self, info):
      try:
          option_items = self.optionitem_set.all()
          return option_items.option_item.name
      except:
          raise Exception("No options items found")