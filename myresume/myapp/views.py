from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html');

def about(request):
    return HttpResponse('about');

def projects(request):
    return HttpResponse('projects');

def contact(request):
    return HttpResponse('contact');