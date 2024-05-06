from django.shortcuts import render, redirect
from .models import Client, Order, Product
from .forms import ProductForm


def client_orders(request, client_id):
    client = Client.objects.get(id=client_id)
    orders = client.order_set.all().order_by('-order_date')
    context = {
        'client': client,
        'orders': orders,
    }
    return render(request, 'client_orders.html', context)


def edit_product(request, product_id):
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})