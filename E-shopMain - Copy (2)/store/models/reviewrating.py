from django.db import models
from django.db.models import Avg

from .category import Category
from .customer import Customer
from .product import Products
class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    username = models.TextField(max_length=10,default = "Username")
    comment = models.TextField(max_length=1000,null=True)
    rating = models.FloatField(default=0,null=True)

    def average_rating(self) -> float:
        return Review.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0
    def __str__(self):
        return self.username
