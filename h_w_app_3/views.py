from django.shortcuts import render
from .models import Client, Order, Product
from datetime import datetime, timedelta


def client_orders(request, client_id):
    client = Client.objects.get(id=client_id)
    orders = client.order_set.all().order_by('-order_date')
    context = {
        'client': client,
        'orders': orders,
    }
    return render(request, 'client_orders.html', context)


def client_ordered_products(request, client_id):
    today = datetime.now()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    year_ago = today - timedelta(days=365)

    orders_week = Order.objects.filter(client_id=client_id, order_date__gte=week_ago).order_by('-order_date')
    orders_month = Order.objects.filter(client_id=client_id, order_date__gte=month_ago).order_by('-order_date')
    orders_year = Order.objects.filter(client_id=client_id, order_date__gte=year_ago).order_by('-order_date')

    context = {
        'orders_week': orders_week,
        'orders_month': orders_month,
        'orders_year': orders_year,
    }
    return render(request, 'ordered_products.html', context)