from django.contrib import admin

from users.models import UserModel


# Register your models here.
@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone_number', 'is_active')  # Customize fields to display
    search_fields = ('username', 'phone_number')  # Enable search functionality
