from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World!")
