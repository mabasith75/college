from django.contrib import admin

# Register your models here.
from . models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'department', 'courses', 'purpose']
    list_editable = ['email', 'department', 'courses']
    prepopulated_fields = {'department': ('name',)}


admin.site.register(Order, OrderAdmin)

