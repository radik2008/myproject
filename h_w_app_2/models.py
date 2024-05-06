"""
Создайте три модели Django: клиент, товар и заказ. Клиент может иметь несколько заказов.
Заказ может содержать несколько товаров. Товар может входить в несколько заказов.
Поля модели "Клиент":
○ имя клиента
○ электронная почта клиента
○ номер телефона клиента
○ адрес клиента
○ дата регистрации клиента

Поля модели "Товар":
○ название товара
○ описание товара
○ цена товара
○ количество товара
○ дата добавления товара

Поля модели "Заказ":
○ связь с моделью "Клиент", указывает на клиента, сделавшего заказ
○ связь с моделью "Товар", указывает на товары, входящие в заказ
○ общая сумма заказа
○ дата оформления заказа
"""
# Create your models here.
from django.db import models


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
