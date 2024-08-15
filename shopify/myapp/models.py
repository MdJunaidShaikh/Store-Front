from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # Product name
    description = models.TextField()  # Product description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Product price
    stock = models.PositiveIntegerField()  # Stock quantity
    available = models.BooleanField(default=True)  # Availability status
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the product was added
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for the last update
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # Product image

    def __str__(self):
        return self.name
