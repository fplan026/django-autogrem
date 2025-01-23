from django.db import models
from django.contrib.auth.models import User

class Budget(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

class Transaction(models.Model):
    name = models.CharField(max_length=30)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE, related_name="transactions")
    category = models.ManyToManyField(Category, related_name="transactions")
    # frequency
    class Meta:
        abstract = True