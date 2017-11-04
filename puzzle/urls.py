from django.conf.urls import url

from puzzle import views

app_name = 'profiles'
urlpatterns = [
    url(r'^$', views.view_home, name='home'),
    url(r'^(?P<pk>[0-9]+)/$', views.view_stage, name='view_stage'),
]
