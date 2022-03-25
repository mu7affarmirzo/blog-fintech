from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from news.models import NewsModel


class NewsView(ListView):
    model = NewsModel
    template_name = 'page/news.html'
    # context_object_name = 'news_list'


# class NewsDetailView(TemplateView):
#     template_name = 'detail.html'