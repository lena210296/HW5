from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default='example@example.com')
    goods = models.ManyToManyField(Goods, related_name='client')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='client')

    def __str__(self):
        return self.name


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=100)
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.supplier_name
