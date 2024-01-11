from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("hello home ")
def about(request):
    return render(request,"about.html")
def contact(request):
    return HttpResponse("hello contact ")
def detail(request):
    return render(request,"detail.html")
def thanks(request):
    return HttpResponse("hello thankyou ")

