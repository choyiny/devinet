from django.conf.urls import url

from puzzle import views

app_name = 'profiles'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/', views.view_home, name='home'),
    url(r'^stage/', views.view_stage, name='view_stage'),
]
