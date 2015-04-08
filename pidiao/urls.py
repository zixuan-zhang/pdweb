from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin

from view import index, product_list, login, upload_file

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pidiao.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', index),
    url(r'^list/$', product_list),
    url(r'^login/', login),
    url(r'^upload/', upload_file),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
