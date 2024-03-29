# Generated by Django 4.2 on 2024-01-29 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("image", models.ImageField(null=True, upload_to="")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("FRUIT", "فاكهة"),
                            ("VEGETABLE", "خضار"),
                            ("SPICE", "تابل"),
                        ],
                        default="FRUIT",
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
