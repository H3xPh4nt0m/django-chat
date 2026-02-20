from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'), #Map the home view to the root URL
    path('accounts/login/', user_login, name='login'), #Map the login view to the /login/ URL
    path('accounts/register/', register, name='register'), #Map the register view to the /register/ URL
    path('accounts/logout/', user_logout, name='logout'), #Map the logout view to the /logout/ URL
    path('search_users/', search_users, name='search_users'), #Map the search view to the /search/ URL
]
