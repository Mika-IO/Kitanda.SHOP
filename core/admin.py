from django.contrib import admin
from core.models import *


class ProductAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


class StoreAdmin(admin.ModelAdmin):
    pass


class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
