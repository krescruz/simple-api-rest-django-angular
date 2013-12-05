from django.conf.urls import patterns, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('app.apps.demo.views',
    # Examples:
    url(r'^$', 'home', name='home_url'),
    url(r'^cadena/$', 'cadena', name='tienda_url'),
    url(r'^tienda/$', 'tienda', name='cadena_url'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
