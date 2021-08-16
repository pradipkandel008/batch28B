from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, blank=True)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    batch = models.IntegerField()
    image_url = models.URLField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.firstname


class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname
