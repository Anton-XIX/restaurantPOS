from django.urls import path

from .views import *

app_name = 'users'

urlpatterns = [

    path('user/', UserListCreateView.as_view()),
    path('user/<str:email>/', UserRetrieveDestroyView.as_view()),
    path('user/update/', UserUpdateView.as_view()),


]