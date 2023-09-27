import uuid
from django.db import models


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CEP = models.CharField(max_length=10)
    road = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)


class PaymentMethod(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)


class Store(models.Model):
    TYPE_CHOICES = [
        ("mercado", "Mercado"),
        ("farmacia", "Farmácia"),
        ("frutaria", "Frutaria"),
        ("outro", "Outro"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="lojas/")
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    slug = models.CharField(max_length=20, null=True)
    whatsapp = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    payment_methods = models.ManyToManyField(PaymentMethod, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True)


class ProductCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="produtos/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, null=True, blank=True
    )
    prescription = models.BooleanField(default=False)


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.ManyToManyField(Address)
    whatsapp = models.CharField(max_length=20)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
