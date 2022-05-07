from django.contrib import admin

from .models import Drinks

@admin.register(Drinks)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('pk','name', 'description')