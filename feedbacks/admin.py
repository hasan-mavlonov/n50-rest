from django.contrib import admin

from feedbacks.models import FeedbackModel


# Register your models here.
@admin.register(FeedbackModel)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'food', 'title', 'text')
    search_fields = ('user', 'food', 'title', 'text')

