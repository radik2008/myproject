from django.db import models
"""
Задание №6
Доработаем задачу про клиентов, заказы и товары из прошлого семинара.
Создайте форму для редактирования товаров в базе данных.

Домашнее задание
Измените модель продукта, добавьте поле для хранения фотографии продукта.
Создайте форму, которая позволит сохранять фото. 
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
    # Добавляем поле для фотографии
    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True)



    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField()

    def __str__(self):
        return f'Order for {self.client} on {self.order_date}'
