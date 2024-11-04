from django.db import models


# Create your models here.
class FoodModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Foods'
        verbose_name = 'Food'


class MenuModel(models.Model):
    restaurant_name = models.CharField(max_length=100)
    dishes = models.ForeignKey(FoodModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant_name

    class Meta:
        ordering = ['restaurant_name']
        verbose_name_plural = 'Menu'
        verbose_name = 'Menu'
