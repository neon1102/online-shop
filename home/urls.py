from django.urls import path
from home.views import home


#  http://127.0.0.1:8000/
#  http://127.0.0.1:8000/home

urlpatterns = [
    path('', home),#home - funksiyadir
    path('home/', home),
]
