from django.urls import include, path
from rest_framework import routers
from apps.store.api import viewsets

router = routers.DefaultRouter()
router.register(r'products', viewsets.ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]