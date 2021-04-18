from django.db import models


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='images/products', blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name
