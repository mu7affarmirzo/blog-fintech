from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class UsersDetailView(TemplateView):
    template_name = 'detail.html'


def tester_func(request):
    return HttpResponse('This is a test')