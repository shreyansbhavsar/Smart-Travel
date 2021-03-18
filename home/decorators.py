from django.shortcuts import render, redirect
from .models import CustomUser
from django.http import HttpResponse


def p_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = request.user.category
        if group == 'Photographer':
            return view_func(request, *args, **kwargs)
        else:
            return render (request,'page404.html')
    return wrapper_func

def g_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = request.user.category
        if group == 'Guide':
            return view_func(request, *args, **kwargs)
        else:
            return render (request,'page404.html')
    return wrapper_func
    
def t_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = request.user.category
        if group == 'Traveller':
            return view_func(request, *args, **kwargs)
        else:
            return render (request,'page404.html')
    return wrapper_func


