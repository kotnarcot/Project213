from django.shortcuts import render
from  .models import Task, Country


def index(request):
    tasks = Task.objects.all()
    return render(request,'main/index.html', {'title':'Главная страница сайта', 'tasks':tasks})

def news(request):
    country = Country.objects.all()
    return render(request,'main/news.html', {'country':country} )

def about(request):
    tasks = Task.objects.all()
    return render(request,'main/about.html', {'tasks':tasks})