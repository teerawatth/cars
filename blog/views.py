from django.shortcuts import render
from .models import *

def index(request):
    return render(request,'index.html')

def buga(request):
    bugattis = bugatti.objects.all()
    return render(request,'buga.html',{
        'bugattis':bugattis
    })

def bugadetail(request):
    return render(request,'bugadetail.html')