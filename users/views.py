from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from users.models import User
from users.serializers import UserSerializer, UserDetailSerializer, UserUpdateSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserListAPIView(ListAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.data['password'])
        user.save()


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserDestroyAPIView(DestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]
