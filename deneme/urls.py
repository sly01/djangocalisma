from django.conf.urls import patterns, include, url

from django.contrib import admin
import views
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^merhaba/', views.merhaba_dunya),
    # Examples:
    # url(r'^$', 'deneme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rastgele/', views.rastgele_sayilar),
    url(r'^dersler/(BT0\d+)/', views.ders_icerikleri),
    url(r'^$', views.ana_sayfa),
    url(r'^ogrenciler/(\d+).html/', views.ogrenci_toplulugu),
    url(r'^ogrenciler/(\d+)/', views.ogrenci_toplulugu),
    url(r'^saat', views.saat)

)
