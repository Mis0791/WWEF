from django.conf.urls import url
from .import views 

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^sponsor/$', views.elf), 
    # url(r'^create$', views.create),
    # url(r'^view/(?P<number>\d+)$', views.view),
    # url(r'^remove/(?P<number>\d+)$', views.remove),
    # url(r'^dashboard$', views.dashboard),
    # url(r'^add/(?P<number>\d+)$', views.add),
    url(r'^logout$', views.logout),
] 