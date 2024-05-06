from django.core.management.base import BaseCommand
from h_w_app_4.models import Client, Product, Order
from faker import Faker
import random
from datetime import datetime

class Command(BaseCommand):
    help = 'Fill the database with sample data'

    def handle(self, *args, **options):
        fake = Faker()

        # Create Clients
        for _ in range(10):
            Client.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                registration_date=fake.date_this_decade(before_today=True)
            )

        # Create Products
        for _ in range(10):
            Product.objects.create(
                name=fake.word(),
                description=fake.text(),
                price=random.uniform(1, 1000),
                quantity=random.randint(1, 100),
                added_date=fake.date_this_decade(before_today=True)
            )

        clients = Client.objects.all()
        products = Product.objects.all()

        # Create Orders
        for _ in range(5):
            client = random.choice(clients)
            products_in_order = random.sample(list(products), random.randint(1, 5))
            total_amount = sum(product.price for product in products_in_order)
            order_date = fake.date_this_decade(before_today=True)
            order = Order.objects.create(
                client=client,
                total_amount=total_amount,
                order_date=order_date
            )
            order.products.set(products_in_order)

        self.stdout.write(self.style.SUCCESS('Database filled with sample data!'))
