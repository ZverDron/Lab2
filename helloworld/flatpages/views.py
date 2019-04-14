#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse(u'Привет, Мир!', mimetype="text/plain")
    return render(request, 'index.html', {})
