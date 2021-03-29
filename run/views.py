from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render, redirect
from run.forms import TeamsForm

# Create your views here.
def about(request):
    return HttpResponse("Hello, world. You're at the about page.")


def home(request):
    return HttpResponse('Hello from home')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def team(request):
    if request.method == "POST":
        form = TeamsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
    else:
        form = TeamsForm()
    return render(request, 'index.html', {'form':form})

def admin(request):
    return render(request, 'admin.html')