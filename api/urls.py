from django.conf.urls import include, url
from api import views





urlpatterns = [
    
    url(r'^tasks/$', views.task_list, name='task_list'),
    #url(r'^tasks/(?P<pk>[0-9]+)$', 'task_detail', name='task_detail'),
   

]
