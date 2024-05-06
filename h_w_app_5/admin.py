from django.contrib import admin

from django.contrib import admin
from .models import Client, Product, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'registration_date')
    list_filter = ('registration_date',)
    search_fields = ('name', 'email', 'phone_number')
    actions = ['send_email']
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone_number')
        }),
        ('Address Info', {
            'fields': ('address',)
        }),
        ('Date Information', {
            'fields': ('registration_date',)
        })
    )

    def send_email(self, request, queryset):
        return None


# Логика отправки email для заказов

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'added_date')
    list_filter = ('added_date',)
    search_fields = ('name', 'description')
    actions = ['send_email']
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Price & Quantity', {
            'fields': ('price', 'quantity')
        }),
        ('Date Information', {
            'fields': ('added_date',)
        })
    )

    def send_email(self, request, queryset):
        return None


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'total_amount', 'order_date')
    list_filter = ('order_date',)
    search_fields = ('client__name', 'products__name')
    actions = ['send_email']
    fieldsets = (
        (None, {
            'fields': ('client', 'products')
        }),
        ('Order Information', {
            'fields': ('total_amount', 'order_date')
        })
    )

    def send_email(self, request, queryset):
        return None
