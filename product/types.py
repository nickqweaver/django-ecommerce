from graphene_django import DjangoObjectType
from product.models import Product

class ProductType(DjangoObjectType):

    class Meta:
        # Reference the model you are accessing
        model = Product
        fields = ('sku', 'name', 'price', 'description', 'weight', 'image', 'thumbnail', 'created_date', 'category', 'stock')
