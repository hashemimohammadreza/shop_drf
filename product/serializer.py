from rest_framework import serializers
from .models import Brand
from .models import Product
from .models import Category

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # یا می‌توانید فیلدهای خاصی را به صورت لیست تعیین کنید





class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'  # یا می‌توانید فیلدهای خاصی را به صورت لیست تعیین کنید