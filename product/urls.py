from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from . import views

router = DefaultRouter()
router.register(r'list_products', views.ProductViewSet, base_name='products')
schema_view = get_swagger_view(title='API Doc')

urlpatterns = [
    url(r'^doc/', schema_view),

    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls), name='api'),
    # url(r'^detail_view/(?P<pk>\d)/$', views.ProductDetailView.as_view(), name='detail_view'),
    # url(r'^list_view/$', views.ProductView.as_view(), name='list_view'),


    url(r'^list_view_category/$', views.CategoryView.as_view(), name='list_view_category'),
    url(r'^detail_view_category/(?P<pk>\d)/$', views.CategoryDetailView.as_view(), name='detail_view_category'),
]

