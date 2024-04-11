from django.db import models
from django.utils import timezone

class Store(models.Model):
    store_id = models.IntegerField(unique=True)
    store_location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.store_id} - {self.store_location}"

class Product(models.Model):
    product_id = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=100)
    product_timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product_id} - {self.product_name}"

class Sale(models.Model):
    transaction_id = models.IntegerField(unique=True)
    transaction_date = models.DateField(default=timezone.now)
    transaction_time = models.TimeField(default=timezone.now)
    transaction_qty = models.IntegerField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.IntegerField()
    product_category = models.CharField(max_length=100)
    product_detail = models.TextField()

    def __str__(self):
        return f"{self.transaction_id} - {self.transaction_date} - {self.transaction_time}"


