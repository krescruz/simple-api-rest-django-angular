from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from rest_framework import routers
from app.apps.api.views import TiendaViewSet, CadenaViewSet
 
router = routers.DefaultRouter()
router.register(r'tiendas', TiendaViewSet)
router.register(r'cadenas', CadenaViewSet)

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'app.apps.api.views.home', name='home'),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
