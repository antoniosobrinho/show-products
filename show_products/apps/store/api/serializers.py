from dataclasses import fields
from rest_framework import serializers
from apps.store.models import Product

class ProductSerializer(serializers.Serializer):

    class Meta:
        model = Product
        exclude = ['updated_at']

    def to_representation(self, instance:Product):
        representation = super().to_representation(instance)
        # representation['product_url'] = instance.image.url
        # representation['product_url__created_at'] = representation['created_at']

        product_sale = instance.productsale_set.all()

        representation['c'] = product_sale.count()

        return representation