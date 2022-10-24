from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def buga(request):
    return render(request,'buga.html')

def bugadetail(request):
    return render(request,'bugadetail.html')