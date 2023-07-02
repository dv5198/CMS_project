from django.urls import path
from .views import UserCreateView, UserDetailView, PostCreateView, PostDetailView, LikeCreateView, LikeDetailView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('posts/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('likes/', LikeCreateView.as_view(), name='like-create'),
    path('likes/<int:pk>/', LikeDetailView.as_view(), name='like-detail'),
]
