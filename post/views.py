from rest_framework import viewsets
from post.models import Post
from post.serializers import PostSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]