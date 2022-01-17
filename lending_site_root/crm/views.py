from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrdersListSerializer


class OrderListView(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrdersListSerializer(orders, many=True)
        return Response(serializer.data)

