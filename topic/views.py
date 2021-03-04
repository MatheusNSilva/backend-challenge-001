from rest_framework import viewsets
from topic.models import Topic
from topic.serializers import TopicSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class TopicsViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


