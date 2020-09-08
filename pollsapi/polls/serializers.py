from polls.models import Question, Choices
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

# class ChoicesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Choices
#         fields = '__all__'

class QuestionDetailSerializer(serializers.ModelSerializer):
    choice = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'
    