from django.conf.urls import patterns, include, url
import yonetim.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'okul.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ogretim-elemanlari-listesi/', yonetim.views.ogretim_elemanlari_listesi),
    url(r'^get-deneme/', yonetim.views.get_deneme),
    url(r'^ogretim-elemani-ekleme', yonetim.views.ogretim_elemani_ekleme),
    url(r'^coklu-ogretim-elemani-ekleme/', yonetim.views.coklu_ogretim_elemani_ekleme),
    url(r'^ders-listesi/', yonetim.views.ders_listesi),
    url(r'^ders-ekleme/', yonetim.views.ders_ekleme),
    url(r'^ogrenci-listesi', yonetim.views.ogrenci_listesi),
    url(r'^ogrenci-ekleme', yonetim.views.ogrenci_ekleme),
    url(r'^yonetim', yonetim.views.yonetim),
)
