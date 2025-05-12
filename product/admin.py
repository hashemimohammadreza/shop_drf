from django.contrib import admin

from product.models import Product, Brand, Category

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)