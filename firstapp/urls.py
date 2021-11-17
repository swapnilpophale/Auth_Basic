from django.urls import path
from .views import *
urlpatterns = [
        path('', signupview, name= 'signup'),
        path('login/', loginview,name= 'login'),
        path('success',loginsuccess, name='loginsuccess'),
        path('logout/',logoutview, name='logout'),
]