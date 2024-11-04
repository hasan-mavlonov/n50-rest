from rest_framework import serializers

from feedbacks.models import FeedbackModel


class FeedbackSerializer(serializers.ModelSerializer):
    giver = serializers.CharField(source='giver.username', read_only=True)

    class Meta:
        model = FeedbackModel
        fields = '__all__'
