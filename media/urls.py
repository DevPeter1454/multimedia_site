from django.urls import path
from .views import image_list

urlpatterns = [
    path('', image_list, name='image_list'),
]
