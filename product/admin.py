from django.contrib import admin
from .models import Waters
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity')
    search_fields = ('name', 'price', 'quantity')
    list_filter = ('price', 'quantity')
    ordering = ('price', )
    
admin.site.register(Waters,ProductAdmin)