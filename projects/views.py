from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def projects_list(request):
    return HttpResponse('This is a projects page')