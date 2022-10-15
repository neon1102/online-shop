from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def home(request):
    #return HttpResponse('<h1>Hello<h1>')
    #template = loader.get_template('index.html')
    return render(request ,'index.html')

