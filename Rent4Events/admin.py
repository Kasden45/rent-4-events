from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ['prodName', 'category', 'quantity', 'available', 'price', 'description', 'image']

admin.site.register(Product, ProductAdmin)