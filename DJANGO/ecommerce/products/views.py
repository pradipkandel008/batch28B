from django.shortcuts import render
from django.http import HttpResponse


def from_app(request):
    return HttpResponse("This is http response from an app")


def second_function(request):
    return HttpResponse("This is http response from an app with second function")
