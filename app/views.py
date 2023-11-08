from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hansi(request):
    return HttpResponse('<h1><marque>hello hansi to entering into hansi:- who are you</marque></h1>')

def bablu(request):
    return HttpResponse('<h1>me:- i am bablu</h1>')