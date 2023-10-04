import uuid
from django.db import models
from django.contrib.auth.models import User
import re


class Store(models.Model):
    TYPE_CHOICES = [
        ("mercado", "Mercado"),
        ("farmacia", "Farmácia"),
        ("frutaria", "Frutaria"),
        ("outro", "Outro"),
    ]

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID"
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Tipo")
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome")
    image = models.ImageField(upload_to="lojas/", verbose_name="Imagem")
    owner = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Proprietário",
    )
    delivery_fee = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Taxa de Entrega"
    )
    slug = models.CharField(max_length=20, null=True, blank=True, verbose_name="Slug")
    whatsapp = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="WhatsApp"
    )
    facebook = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Facebook"
    )
    instagram = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Instagram"
    )
    address = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Endereço"
    )
    city = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        default="Ariquemes",
        verbose_name="Cidade",
    )
    UF = models.CharField(
        max_length=2, null=True, blank=True, default="RO", verbose_name="Estado"
    )

    def save(self, *args, **kwargs):
        self.slug = re.sub(r"\s+", "-", self.name.lower())
        super(Store, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Lojas"
        verbose_name = "Loja"
        db_table = "core_store"


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID"
    )
    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    image = models.ImageField(upload_to="produtos/", verbose_name="Imagem")
    store = models.ForeignKey(
        Store,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Loja",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Produtos"
        verbose_name = "Produto"
        db_table = "core_product"


class Order(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("preparando", "Preparando"),
        ("em_entrega", "Em Entrega"),
        ("concluido", "Concluído"),
    ]

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID"
    )
    store = models.ForeignKey("Store", on_delete=models.CASCADE, verbose_name="Loja")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pendente", verbose_name="Status"
    )

    content = models.TextField(verbose_name="Conteúdo")

    delivery_fee = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Taxa de Entrega"
    )
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Subtotal"
    )
    total = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Total"
    )

    def update_total(self):
        total_price = sum(
            item.product.price * item.quantity for item in self.order_items.all()
        )
        self.total = total_price
        self.save()

    def __str__(self):
        client_name = dict(self.content)["address"]["nome"]
        return f"{client_name} {self.total}"

    class Meta:
        verbose_name_plural = "Pedidos"
        verbose_name = "Pedido"
        db_table = "core_order"
