from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def index(request):
    data = {'title' : 'Главная страница',
            'time' : datetime.datetime.now()}
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')