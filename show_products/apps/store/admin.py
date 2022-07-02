from django.contrib import admin
from apps.store.models import Product, ProductSale

# Register your models here.

class ProductSaleAdmin(admin.TabularInline):

    model = ProductSale
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    inlines = (ProductSaleAdmin, )