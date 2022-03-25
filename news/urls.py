from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path('main/', NewsView.as_view(), name='main-news-page')
]