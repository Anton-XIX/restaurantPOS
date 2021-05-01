from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from .permissions import IsOwnerOrReadOnly, CanGetListUser
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from .models import *
from .serializers import UserUpdateSerializer, ChangePasswordSerializer


# class UserListCreateView(ListCreateAPIView):
#     queryset = CustomUser.objects.all().order_by('is_active')
#     serializer_class = UserSerializer
#     permission_classes = [CanGetListUser | IsAdminUser]
#     filterset_fields = ['email', 'phone_number']
#
#
# class UserRetrieveDestroyView(RetrieveAPIView, DestroyAPIView):
#     lookup_field = 'email'
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser | IsOwnerOrReadOnly]


class UserUpdateView(UpdateAPIView):
    lookup_field = 'email'
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save
        return Response('Password changed')
