from graphene_django import DjangoObjectType
from graphene import Field, List, String, ObjectType
from product.models import Product 

class ProductOption(ObjectType):
    option_category = String()
    options = List(String)

class ProductType(DjangoObjectType):
    product_options = List(ProductOption)

    class Meta:
        # Reference the model you are accessing
        model = Product

    def resolve_product_options(self, info):
        options = []
        
        try:
            product_option_set = self.productoption_set.all()
            option_categories = []
            product_options = []

            for option_item in product_option_set:
                option_categories.append(option_item.option_item.option.name)

            unique_option_categories = set(option_categories)

            for unqiue_option_cateogry in unique_option_categories:
                product_options_queryset = product_option_set.filter(option_item__option__name=unqiue_option_cateogry)
                filtered_product_options = []

                for product_option in product_options_queryset:
                    filtered_product_options.append(product_option.option_item.name)
                
                product_options.append(ProductOption(option_category=unqiue_option_cateogry, options=filtered_product_options))
            return product_options
        except:
            raise Exception("No product options found for this product")