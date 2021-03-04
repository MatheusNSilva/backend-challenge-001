from rest_framework import viewsets
from comment.models import Comment
from comment.serializers import CommentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

