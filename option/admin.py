from django.contrib import admin
from option.models import Option, OptionItem, ProductOption, BrandOption, ProductBrandOption
# Register your models here.
admin.site.register(Option)
admin.site.register(OptionItem)
admin.site.register(ProductOption)
admin.site.register(BrandOption)
admin.site.register(ProductBrandOption)
