from django.contrib import admin

from .models import Drinks, Category

@admin.register(Drinks)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('pk','category','name', 'description', 'created')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description','created')