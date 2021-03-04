from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from topic.views import TopicsViewSet
from post.views import PostViewSet
from comment.views import CommentViewSet


router = routers.DefaultRouter()
router.register('topic', TopicsViewSet, basename='Topics')
router.register('post', PostViewSet, basename='Posts')
router.register('comment', CommentViewSet, basename='Comments')

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('topic/', TopicsViewSet.as_view({'get':'list'})),
    path('topic/<int:pk>', TopicsViewSet.as_view({'get':'list'})),
    path('topic/post/', TopicsViewSet.as_view({'get': 'list'})),
    path('topic/post/<int:pk>', PostViewSet.as_view({'get': 'list'})),
    path('topic/post/comment/', CommentViewSet.as_view({'get': 'list'})),
    path('topic/post/comment/<int:pk>', CommentViewSet.as_view({'get': 'list'})),
]