from rest_framework import serializers

from dishes.models import MenuModel


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = '__all__'
