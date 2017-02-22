from django.conf.urls import url
from media import views

urlpatterns = [

    url(r'^video/$', views.lst),
    url(r'^video/cad/', views.cad),
    url(r'^video/edit/(?P<id>\d+)$', views.edit),
    url(r'^video/delete/(?P<id>\d+)$', views.delete),

]