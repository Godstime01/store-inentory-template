from django.contrib import admin
from .models import Item
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
          list_display = ['name', 'price', 'expiry_date', 'quantity']
          
admin.site.register(Item)