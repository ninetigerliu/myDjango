# from django.http import HttpResponse
#
# def hello(request):
#     return HttpResponse("Hello world ! ")


# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {}
    context['hello'] = 'Hello World! Xiao\'s first line of Django code'
    return render(request, 'hello.html', context)
