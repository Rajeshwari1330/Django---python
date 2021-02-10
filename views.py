# This file is created by me.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'Misti', 'Place':'Mars'}
    return render(request, 'index.html', params)

def removepunc(request):
    return HttpResponse("Remove Punctuation")

def capfirst(request):
    return HttpResponse("capitalize First")

def newlineremove(request):
    return HttpResponse("New Line Remove")

def spaceremove(request):
    return HttpResponse("Space Remove <a href = '/' > back </a> ")

def charcount(request):
    return HttpResponse("Character Count")
