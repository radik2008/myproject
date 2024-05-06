from django.urls import path
from . import views

urlpatterns = [
    path('client_orders1/<int:client_id>/', views.client_orders, name='client_orders'),
    path('<int:product_id>/edit_product/', views.edit_product, name='edit_product'),
    path('add_product/', views.add_product, name='add_product'),

]
