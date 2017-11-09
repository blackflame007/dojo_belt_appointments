from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^appointments$', views.appointments),
    url(r'^change/(?P<task_id>\d+)$', views.change),
    url(r'^appointments/(?P<task_id>\d+)$', views.update),
    url(r'^delete/(?P<task_id>\d+)$', views.delete),
    url(r'^new_appointment$', views.new_appointment),

]
 