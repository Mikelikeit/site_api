from django.urls import path

from . import views

urlpatterns = [
    path('crm/', views.OrderListView.as_view())
]
