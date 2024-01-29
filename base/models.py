from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(null=True)
    PRODUCT_TYPES = [("FRUIT", "فاكهة"), ("VEGETABLE", "خضار"), ("SPICE", "تابل")]
    type = models.CharField(max_length=10, choices=PRODUCT_TYPES, default="FRUIT")

    def __str__(self):
        return self.name