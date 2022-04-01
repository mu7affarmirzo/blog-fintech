from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from news.models import NewsModel


class NewsView(ListView):
    model = NewsModel
    template_name = 'page/news.html'
    context_object_name = 'news_list'


class NewsDetailView(DetailView):
    model = NewsModel
    template_name = 'page/detail-page.html'
    context_object_name = 'news'


class AddNewsView(CreateView):
    model = NewsModel
    template_name = 'page/add-news.html'
    fields = ['title', 'body', 'author', 'image']


class UpdateNewsView(UpdateView):
    model = NewsModel
    template_name = 'page/update-news.html'
    fields = ['title', 'body', 'image']


class DeleteNewsView(DeleteView):
    model = NewsModel
    template_name = 'page/delete-news.html'
    context_object_name = 'news'
    success_url = reverse_lazy('news:main-news-page')

