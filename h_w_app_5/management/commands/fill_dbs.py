from django.core.management.base import BaseCommand
from h_w_app_5.models import Client, Product, Order
from django.utils import timezone
from decimal import Decimal

class Command(BaseCommand):
    help = 'Fill the database with sample data'

    def handle(self, *args, **options):
        # Create clients
        client1 = Client.objects.create(name='John Doe', email='john@example.com', phone_number='1234567890', address='123 Main St', registration_date=timezone.now())
        client2 = Client.objects.create(name='Jane Smith', email='jane@example.com', phone_number='9876543210', address='456 Elm St', registration_date=timezone.now())

        # Create products
        product1 = Product.objects.create(name='Product 1', description='Description for Product 1', price=Decimal('10.00'), quantity=100, added_date=timezone.now())
        product2 = Product.objects.create(name='Product 2', description='Description for Product 2', price=Decimal('20.00'), quantity=50, added_date=timezone.now())

        # Create orders
        order1 = Order.objects.create(client=client1, total_amount=Decimal('30.00'), order_date=timezone.now())
        order1.products.add(product1)

        order2 = Order.objects.create(client=client2, total_amount=Decimal('40.00'), order_date=timezone.now())
        order2.products.add(product1, product2)

        self.stdout.write(self.style.SUCCESS('Database filled with sample data'))