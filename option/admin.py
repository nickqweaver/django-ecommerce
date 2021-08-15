from django.contrib import admin
from option.models import Option, OptionItem, ProductOption
# Register your models here.
admin.site.register(Option)
admin.site.register(OptionItem)
admin.site.register(ProductOption)
