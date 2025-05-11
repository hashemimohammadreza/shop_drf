import mptt
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Brand(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True, null=False)
    parent = TreeForeignKey('self', null=True, blank=True, on_delete=models.PROTECT)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name