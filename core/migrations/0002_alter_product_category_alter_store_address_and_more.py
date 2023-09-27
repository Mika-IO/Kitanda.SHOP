# Generated by Django 4.2.4 on 2023-09-26 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.productcategory",
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="address",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.address",
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="delivery_fee",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="store",
            name="facebook",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="store",
            name="instagram",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="store",
            name="payment_methods",
            field=models.ManyToManyField(blank=True, to="core.paymentmethod"),
        ),
        migrations.AlterField(
            model_name="store",
            name="type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("mercado", "Mercado"),
                    ("farmacia", "Farmácia"),
                    ("frutaria", "Frutaria"),
                    ("outro", "Outro"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="whatsapp",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
