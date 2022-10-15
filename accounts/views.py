from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def loginView(request):
    if request.method == 'Post':
        name = request.Post.get('next','/')
        password = request.POST.GET('password')
    
    return render(request, 'login.html')

# Create your views here.
