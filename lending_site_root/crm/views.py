from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Orders, Products
from .serializers import OrdersListSerializer, ProductsListSerializer


class OrdersListView(APIView):
    '''Вывод списка заказов'''

    def get(self, request):
        orders = Orders.objects.all()
        serializer = OrdersListSerializer(orders, many=True)
        return Response(serializer.data)


class ProductsListView(APIView):
    '''Вывод списка продуктов'''

    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsListSerializer(products, many=True)
        return Response(serializer.data)
