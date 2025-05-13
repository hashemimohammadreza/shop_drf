from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


from product.views import BrandsView, ProductView, CategoryView

route = DefaultRouter()
route.register("brands", BrandsView)
route.register('products', ProductView)
route.register('category', CategoryView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/doc/', SpectacularRedocView.as_view(url_name='schema'), name='doc'),

]
