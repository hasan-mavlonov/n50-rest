from django.db import models

from users.models import UserModel
from dishes.models import FoodModel


# Create your models here.
class FeedbackModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    food = models.ForeignKey(FoodModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'
