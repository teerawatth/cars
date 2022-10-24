from django.shortcuts import render
from .models import *

def index(request):
    return render(request,'index.html')

def buga(request):
    bugattis = bugatti.objects.all()
    return render(request,'buga.html',{
        'bugattis':bugattis
    })

def bugadetail(req,pk):
    product = bugatti.objects.get(id=pk)
    return render(req,'bugadetail.html',{
        'product':product,

    })

def koenig(request):
    koenigseggs = koenigsegg.objects.all()
    return render(request,'koenig.html',{
        'koenigseggs':koenigseggs
    })

def koenigdetail(req,pk):
    product = koenigsegg.objects.get(id=pk)
    return render(req,'koenigdetail.html',{
        'product':product,

    })