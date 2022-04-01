from django.urls import path
from news.views import *

app_name = 'news'

urlpatterns = [
    path('', NewsView.as_view(), name='main-news-page'),
    path('detail/<int:pk>', NewsDetailView.as_view(), name='detail-news-page'),
    path('add/', AddNewsView.as_view(), name='add-news-page'),
    path('update/<int:pk>/edit', UpdateNewsView.as_view(), name='update-news-page'),
    path('delete/<int:pk>', DeleteNewsView.as_view(), name='delete-news-page'),
]