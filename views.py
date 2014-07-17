from django.http import *
from django.template import Template, Context
import random
from time import ctime
from django.template.loader import get_template
from django.shortcuts import render_to_response
def rastgele_sayilar(request):
    return HttpResponse('<b>Rastgele bir sayi: </b> %f' % random.random())
def test(request):
    return HttpResponse('%f' % random.random())
def merhaba_dunya(request):
    return HttpResponse(u'Merhaba Dunya')
def isim_soyisim(request):
    return HttpResponse('<h1>Ahmet Erkoc</h1><br> <p>Merhaba ben Ahmet ERKOC</p>')

def ders_icerikleri(request, ders_kodu):
    dersler = {'BTO101': 'Egitimde Bilisim Teknolojileri',
               'BTO102': 'Matematik 1',
               'BTO103': 'Matematik 2',
               'BTO104': 'Coklu ortam Tasarimi ve Uretimi'}
    if not ders_kodu in dersler:
        #return HttpResponse('<b>%s</b> kodlu bir ders yok' % ders_kodu)
        raise Http404("Tanimli olmayan bir ders icerigine erismeye calisiyorsun")
    else:
        html = '<b>%s</b> kodlu dersin adi <b>%s</b>, icerigi sonra gelecek.' % (ders_kodu, dersler[ders_kodu])
        return HttpResponse(html)

def ana_sayfa(request):
    return HttpResponse('<h1>Ana Sayfa</h1>Burasi Django Ana Sayfasidir.')

def ogrenciler(request, no):
    ogr = {'12': ('Fatih Baser', 'Kimya Ogretmenligi'),
           '25': ('Aybuke Alayli', 'Biyoloji'),
           '49': ('Enes Sunbul', 'Cografya')
           }
    html = '<b>Ogrencinin Adi:</b> %s <br/><b>Bolumu:</b>%s' % (ogr[no][0], ogr[no][1])
    return HttpResponse(html)

def saat(request):
    return HttpResponse(ctime())

def ogrencilistesi(request):
    ogrenciler = (('Selim', 'Yildirim', 20, 40),
                 ('Melike', 'Baser', 40, 60),
                 ('Aybuke', 'Abayli', 50, 30),
                 ('Enes', 'Sunbul', 60, 50))
    '''s = get_template('ogrencilistesi.html')
    b = Context({'ogrenciler': ogrenciler})
    html = s.render(b)
    return HttpResponse(html)'''
    #return render_to_response('ogrencilistesi.html', {'ogrenciler': ogrenciler})
    sayfa_basligi = 'Ogrenci Listesi'
    simdiki_zaman = ctime()
    return render_to_response('ogrencilistesi.html',locals())

