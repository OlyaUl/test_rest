from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list_view/$', views.ProductView.as_view(), name='list_view'),
]