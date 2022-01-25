from rest_framework import serializers

from .models import Orders, Products


class OrdersListSerializer(serializers.ModelSerializer):
    '''Список заказов'''

    employee = serializers.SlugRelatedField(slug_field='last_name', read_only=True)
    ship_via = serializers.SlugRelatedField(slug_field='company_name', read_only=True)

    class Meta:
        model = Orders
        fields = ('__all__')


class ProductsListSerializer(serializers.ModelSerializer):
    '''Список продуктов'''

    supplier = serializers.SlugRelatedField(slug_field='company_name', read_only=True)
    category = serializers.SlugRelatedField(slug_field='category_name', read_only=True)

    class Meta:
        model = Products
        fields = ('__all__')
