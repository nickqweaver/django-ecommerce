# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models
from order.models import Order

class AddressInline(admin.StackedInline):
    model = models.Address

class OrdersInline(admin.StackedInline):
  model = Order

class CustomProfileAdmin(admin.ModelAdmin):
  inlines = [AddressInline, OrdersInline]

admin.site.register(models.Profile, CustomProfileAdmin)


class ProfileInline(admin.StackedInline):
    model = models.Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(models.Customer, CustomUserAdmin)
