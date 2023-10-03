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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="lojas/")
    owner = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Owner",
    )
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    slug = models.CharField(max_length=20, null=True, blank=True)
    whatsapp = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    city = models.CharField(max_length=100, null=True, blank=True, default="Ariquemes")
    UF = models.CharField(max_length=2, null=True, blank=True, default="RO")

    def save(self, *args, **kwargs):
        self.slug = re.sub(r"\s+", "-", self.name.lower())
        super(Store, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="produtos/")
    store = models.ForeignKey(
        Store,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Owner",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("preparando", "Preparando"),
        ("em_entrega", "Em Entrega"),
        ("concluido", "Concluído"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey("Store", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pendente")

    content = models.TextField()

    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def update_total(self):
        total_price = sum(
            item.product.price * item.quantity for item in self.order_items.all()
        )
        self.total = total_price
        self.save()

    def __str__(self):
        return f"{self.client.name} {self.total}"
