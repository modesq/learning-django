from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="data", blank=True, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to="assets/Products/")
