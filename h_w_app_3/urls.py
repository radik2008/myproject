from django.urls import path
from . import views

urlpatterns = [
    path('client_orders1/<int:client_id>/', views.client_orders, name='client_orders'),
    path('client_orders2/<int:client_id>/', views.client_ordered_products, name='client_ordered_products'),
]
