from django.urls import path

from . import views

urlpatterns = [
    path('orders/', views.OrdersListView.as_view()),
    path('products/', views.ProductsListView.as_view())
]
