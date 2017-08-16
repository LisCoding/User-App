from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^/(?P<id>\d+)$', views.show),
    url(r'^/new$', views.new),
    url(r'^/(?P<id>\d+)/edit$', views.edit),
    url(r'^/update/(?P<id>\d+)$', views.update),
    url(r'^/create$', views.create),
    url(r'^/(?P<id>\d+)/delete$', views.delete)
]
#
# url(r'^/(?P<number>\d+)$', views.show),
# url(r'^/(?P<number>\d+)/edit$', views.edit),
# url(r'^/(?P<number>\d+)/delete$', views.destroy)
