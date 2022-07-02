from rest_framework import serializers
from apps.store.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance:Product):
        representation = super().to_representation(instance)
        representation['product_url'] = instance.image.url
        representation['product_url__created_at'] = representation['created_at']

        product_sale = instance.productsale_set.all()

        representation['c'] = product_sale.count()

        return representation