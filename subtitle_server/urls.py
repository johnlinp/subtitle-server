from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'provider.views.portal'),
    url(r'^edit/(?P<video_id>\d+)$', 'provider.views.edit'),

    url(r'^login/$', 'provider.views.login'),
    url(r'^create/$', 'provider.views.create'),
    url(r'^retrieve/$', 'provider.views.retrieve'),
    url(r'^upload-subt/$', 'provider.views.upload_subt'),

    url(r'^demo/$', 'player.views.demo'),

    # Examples:
    # url(r'^$', 'subtitle_server.views.home', name='home'),
    # url(r'^subtitle_server/', include('subtitle_server.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
