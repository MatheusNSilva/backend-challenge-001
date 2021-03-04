from rest_framework import serializers
from topic.models import Topic


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'created_at', 'updated_at']