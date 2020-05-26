from .models import Topic, Content
from rest_framework import serializers

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)

    class Meta:
        model = Topic
        fields = ['id', 'topic', 'contents']