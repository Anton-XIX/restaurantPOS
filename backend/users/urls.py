from django.urls import path

from .views import UserUpdateView, ChangePasswordView # UserListCreateView, UserRetrieveDestroyView,


urlpatterns = [

    # path('', UserListCreateView.as_view()),
    # path('<str:email>/', UserRetrieveDestroyView.as_view()),
    path('update/', UserUpdateView.as_view()),
    path('change_password', ChangePasswordView.as_view())


]