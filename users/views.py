from django.shortcuts import render
from django.views.generic import TemplateView


class UsersDetailView(TemplateView):
    template_name = 'detail.html'