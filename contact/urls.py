
from cgi import test
from django.urls import path
from contact.views import contactView, test1


urlpatterns = [
    path('', contactView, name='contact'),
    path("test/", test1)
]
