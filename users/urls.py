from django.urls import path
from users.views import UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, UserListAPIView, UserDestroyAPIView

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('user/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('user/detail/', UserRetrieveAPIView.as_view(), name='user-detail'),
    path('user/edit/', UserUpdateAPIView.as_view(), name='user-edit'),
    path('user/delete/<int:pk>', UserDestroyAPIView.as_view(), name='user-delete'),
]
