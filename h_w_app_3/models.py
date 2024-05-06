from django.db import models
"""
Задание №7
Доработаем задачу 8 из прошлого семинара про клиентов, товары и заказы.
Создайте шаблон для вывода всех заказов клиента и списком товаров внутри каждого заказа.
Подготовьте необходимый маршрут и представление.

Продолжаем работать с товарами и заказами.
Создайте шаблон, который выводит список заказанных
клиентом товаров из всех его заказов с сортировкой по
времени:
○ за последние 7 дней (неделю)
○ за последние 30 дней (месяц)
○ за последние 365 дней (год)
*Товары в списке не должны повторятся.
"""

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateField()

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()

    def __str__(self):
        return f'Order for {self.client} on {self.order_date}'
