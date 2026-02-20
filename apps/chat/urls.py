from django.urls import path
from .views import *

urlpatterns = [
   path('<str:username>/', ChatRoom, name='ChatRoom'),
]