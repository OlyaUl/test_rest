from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list_view/$', views.ProductView.as_view(), name='list_view'),
    url(r'^detail_view/(?P<pk>\d)/$', views.ProductDetailView.as_view(), name='detail_view'),
    url(r'^list_view_category/$', views.CategoryView.as_view(), name='list_view_category'),
    url(r'^detail_view_category/(?P<pk>\d)/$', views.CategoryDetailView.as_view(), name='detail_view_category'),
]