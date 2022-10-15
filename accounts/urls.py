from django.urls import path
from accounts.views import  loginView


urlpatterns = [
    path('login/',loginView, name = 'login')
]