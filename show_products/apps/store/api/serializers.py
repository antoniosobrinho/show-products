from django.db.models import Count
from rest_framework import serializers
from apps.store.models import Product

class (serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance:Product):
        representation = super().to_representation(instance)
        representation['product_url'] = representation['image']
        representation['product_url__created_at'] = representation['created_at']

        product_sale = instance.productsale_set.all()

        representation['c'] = product_sale.count()
        representation['consult_date'] = list()
        product_sale_count = product_sale.order_by(
                                        'date_of_sale'
                                    ).values(
                                        'date_of_sale'
                                    ).annotate(dcount=Count('date_of_sale'))

        for count in product_sale_count:
            representation['consult_date'].append(
                {
                    'date_of_sale': count['date_of_sale'].strftime('%d/%m/%Y'),
                    'count': count['dcount']
                }
            )
        return representation