from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def lesson1(request):
    return render(request, 'main/lesson1.html')

def lesson2(request):
    return render(request, 'main/lesson2.html')
