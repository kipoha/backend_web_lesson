from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse('Hello! Its my project')

def current_date(request):
    date = datetime.datetime.now()
    text = date.strftime('%d.%m.%Y')
    return HttpResponse(f'Current date: {text}')

def goodby(request):
    return HttpResponse('Goodby user!')