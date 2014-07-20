from django.conf.urls import patterns, include, url
import kitap.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kitapcilar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^yazarlar/', kitap.views.yazarlar),
    url(r'^kitaplar/(\d+)/', kitap.views.kitaplar),
)
