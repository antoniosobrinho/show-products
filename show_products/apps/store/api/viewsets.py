import imp
from rest_framework import viewsets
from apps.store.models import Product
from apps.store.api.serializers import ProductSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer