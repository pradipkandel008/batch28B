from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, blank=True)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name

