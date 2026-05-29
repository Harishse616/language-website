from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def ah(request):
    return render(request, "ah.html")
