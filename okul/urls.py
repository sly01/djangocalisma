from django.conf.urls import patterns, include, url
from yonetim import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'okul.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ogretim-elemanlari-listesi/',views.ogretim_elemanlari_listesi),
    url(r'^get-deneme/', views.get_deneme),
    url(r'^ogretim-elemani-ekleme', views.ogretim_elemani_ekleme),
    url(r'^coklu-ogretim-elemani-ekleme/', views.coklu_ogretim_elemani_ekleme),
    url(r'^ders-listesi/', views.ders_listesi),
    url(r'^ders-ekleme/', views.ders_ekleme),
    url(r'^ogrenci-listesi', views.ogrenci_listesi),
    url(r'^ogrenci-ekleme', views.ogrenci_ekleme),
    url(r'^yonetim', views.yonetim),
    url(r'^cerez-deneme', views.cerez_deneme),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'}),
)
