from django.contrib import admin
from django import forms
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
    readonly_fields = (
        "store",
        "delivery_fee",
        "subtotal",
        "total",
        "formatted_content",
    )
    exclude = ("content",)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Limita as opções de lojas disponíveis para o owner
        if db_field.name == "store":
            kwargs["queryset"] = Store.objects.filter(owner=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(store__owner=request.user)
        return qs

    def formatted_content(self, instance):
        try:
            # Carrega o JSON em um dicionário Python
            data = json.loads(instance.content.replace("'", '"'))

            # Formata a lista de produtos
            products_list = ""
            for product in data.get("cart", []):
                product_info = f"- {product['quantity']}x {product['product_name']}  R${product['product_price']}\n"
                products_list += product_info

            # Formata o endereço com rótulos
            address = f"Endereço:\n"
            address += f"  - Rua: {data.get('address', {}).get('rua', '')}\n"
            address += f"  - Bairro: {data.get('address', {}).get('bairro', '')}\n"
            address += f"  - Número: {data.get('address', {}).get('numero', '')}\n"
            address += (
                f"  - Complemento: {data.get('address', {}).get('complemento', '')}\n"
            )

            address += f"Cliente: {data.get('address', {}).get('nome', '')}\n"

            # Formata o restante das informações
            formatted_content = f"Produtos:\n{products_list}\n{address}"
        except json.JSONDecodeError:
            # Trata caso o JSON não seja válido
            formatted_content = "Conteúdo inválido"

        return formatted_content

    formatted_content.short_description = "Content"


admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Order, OrderAdmin)
