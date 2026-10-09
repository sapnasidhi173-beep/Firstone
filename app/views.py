from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Gyan(request):
    return HttpResponse("Hello Gyan, Welcome to Django")