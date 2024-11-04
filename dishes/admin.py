from django.contrib import admin

from dishes.models import FoodModel, MenuModel


@admin.register(FoodModel)
class FoodModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(MenuModel)
class MenuModelAdmin(admin.ModelAdmin):
    list_display = ('restaurant_name', 'dishes')
