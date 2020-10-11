from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django import template

# Create your views here.
def home(request):
    #return HttpResponse(u'Привет, Мир!', content_type="text/plain", charset="cp1251")
    #return HttpResponse(u'Привет, Мир!', charset="cp1251")
    #return render(request, 'templates/index.html')
    return render(request, 'templates/static_handler.html')
