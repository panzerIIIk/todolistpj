from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>hello Django!hello my friend</h1>")


def profile(request):
    context = {
        "name": "tim",
        "age": 35,
        "height": 170,
        "weight": 85,
    }

    return JsonResponse(context)
