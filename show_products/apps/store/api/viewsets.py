from rest_framework import viewsets, filters
from apps.store.models import Product
from apps.store.api.serializers import ProductSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
    ordering = ['created_at']