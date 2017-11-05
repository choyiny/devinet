from django.conf.urls import url

from puzzle import views

app_name = 'puzzle'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/', views.view_list, name='list'),
    url(r'^stage/stagecomplete/', views.setStageStatus, name='stage_complete'),
    url(r'^home/', views.view_home, name='home'),
    url(r'^stage/', views.view_stage, name='view_stage'),
]
