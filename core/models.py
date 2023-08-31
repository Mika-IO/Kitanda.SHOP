import uuid
from django.db import models

class TipoLoja(models.Model):
    TIPO_CHOICES = [
        ('mercado', 'Mercado'),
        ('farmacia', 'Farmácia'),
        ('frutaria', 'Frutaria'),
        ('outro', 'Outro'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

class Loja(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tipo = models.ForeignKey(TipoLoja, on_delete=models.CASCADE)
    address = models.TextField()
    name = models.CharField(max_length=100)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
    whatsapp = models.CharField(max_length=20)
    facebook = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    PAYMENT_CHOICES = [
        ('na_entrega', 'Na Entrega'),
        ('cartao_credito', 'Cartão de Crédito'),
        ('cartao_debito', 'Cartão de Débito'),
        ('pix', 'PIX'),
    ]
    payment_methods = models.CharField(max_length=20, choices=PAYMENT_CHOICES)

class ProductCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    prescription = models.BooleanField(default=False)

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    prescription = models.BooleanField(default=False)

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    products = models.ManyToManyField(Product)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)

class Checkout(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    address = models.TextField()
    whatsapp = models.CharField(max_length=20)

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CEP = models.CharField(max_length=10)
    road = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
