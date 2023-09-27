import uuid
from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    TYPE_CHOICES = [
        ("mercado", "Mercado"),
        ("farmacia", "Farmácia"),
        ("frutaria", "Frutaria"),
        ("outro", "Outro"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="lojas/")
    owner = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE,
        verbose_name="Owner",
    )
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    slug = models.CharField(max_length=20, null=True)
    whatsapp = models.CharField(max_length=20, null=True)
    facebook = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)


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


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    whatsapp = models.CharField(max_length=20)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
