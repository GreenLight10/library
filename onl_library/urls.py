from django.urls import path
from .views import *

# app_name = 'onl_library'

urlpatterns = [
    path('', base, name='base'),
    path('books/', books, name='books'),
    path('login/', LoginUser.as_view(), name='login'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('logout/', logout_user, name='logout'),
    path('favourites/', favourite_list, name='favourite_list'),
    path('favourites/<int:id>/', favourite_add, name='favourite_add'),
]
