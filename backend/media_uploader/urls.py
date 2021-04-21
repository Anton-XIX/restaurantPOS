from django.urls import path
from .views import ImageCreateView


urlpatterns = [

    path('media/image', ImageCreateView.as_view()),

]
