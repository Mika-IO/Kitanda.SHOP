from django.contrib import admin
from core.models import *


class StoreAdmin(admin.ModelAdmin):
    exclude = ("owner", "slug")

    def save_model(self, request, obj, form, change):
        if getattr(obj, "owner", None) is None:
            obj.owner = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super(StoreAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(owner=request.user)
        return qs


class ProductAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Limita as opções de lojas disponíveis para o owner
        if db_field.name == "store":
            kwargs["queryset"] = Store.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super(ProductAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            # Filtra os produtos para aqueles pertencentes às lojas do usuário atual
            qs = qs.filter(store__owner=request.user)
        return qs


class OrderAdmin(admin.ModelAdmin):
    pass


class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
