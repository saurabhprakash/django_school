from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

import core.views as core_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', core_views.HomeView.as_view(), name='home'),
    # url(r'^school/', include('school.foo.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

	# Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^(?P<page_name>\w+)$', core_views.PageView.as_view(), name='home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
