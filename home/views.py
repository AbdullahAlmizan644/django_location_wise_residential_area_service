from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "main/index.html")


def rent(request):
    return render(request, "main/rent.html")


def about(request):
    return render(request, "main/about.html")


def contact(request):
    return render(request, "main/contact.html")


def teacher(request):
    return render(request, "main/teacher.html")


def tution(request):
    return render(request, "main/tution.html")


