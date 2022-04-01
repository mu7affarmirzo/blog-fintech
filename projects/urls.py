from django.urls import path
from projects.views import projects_list

app_name = 'projects'

urlpatterns = [
    path('', projects_list, name='list-projects')
]