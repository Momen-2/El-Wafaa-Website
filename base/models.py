from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    name = models.CharField(max_length = 150)
    image = models.ImageField(null=True)
    PRODUCT_TYPES = [("FRUIT", "فاكهة"), ("VEGETABLE", "خضار"), ("SPICE", "تابل")]
    type = models.CharField(max_length=10, choices=PRODUCT_TYPES, default="FRUIT")
    slug = models.SlugField(max_length=900, blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)