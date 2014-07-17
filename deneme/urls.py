from django.conf.urls import patterns, include, url
import views
import blog.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deneme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^merhaba/', views.merhaba_dunya),
    url(r'^kimsin/', views.isim_soyisim),
    url(r'^rastgele/', views.rastgele_sayilar),
    url(r'^test/', views.test),
    url(r'^dersler/(BTO\d+)/', views.ders_icerikleri),
    url(r'^$', views.ana_sayfa),
    url(r'^ogrenciler/(\d+).html/', views.ogrenciler),
    url(r'^zaman/', views.saat),
    url(r'^ogrencilistesi/', views.ogrencilistesi),
    url(r'^postlistesi/', blog.views.index),
)
