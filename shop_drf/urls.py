
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from product.models import Category
from product.views import BrandsView, ProductView, CategoryView

route=DefaultRouter()
route.register("brands",BrandsView)
route.register('products', ProductView)
route.register('category', CategoryView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),

]



