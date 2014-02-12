# -*- coding: utf-8 -*-

from django.http import *
from datetime import datetime
import random

def merhaba_dunya(request):
	return HttpResponse('<h1>Merhaba Dunya</h1>')

def rastgele_sayilar(request):
	return HttpResponse('<b>Rastegele bir sayi: </b> %f' % random.random())

def ders_icerikleri(request, ders_kodu):
	dersler={'BT0101': u'Egitimde Bilisim Teknolojileri',
	'BT0103': u'Matemaik 1',
	'BT0104': u'Matematik 2',
	'BT0302': u'Coklu ortam Tasarimi ve Uretimi'
	}
	if not ders_kodu in dersler:
		raise Http404("Tanimli olmayan bir ders icerigine erismeye calisiyorsunuz")
	else:
		html=u'<b>%s</b> kodlu dersin adi <b>%s</b>, icerigi sonra gelecek.' % (ders_kodu,dersler[ders_kodu])
		return HttpResponse(html)

def ana_sayfa(request):
	return HttpResponse('<h1>Ana Sayfa</h1> Burasi Django Ana Sayfasidir.')

def ogrenci_toplulugu(request, ogrenci_no):
	ogr={'12': ('Fatih Baser', 'Kimya Ogretmenligi'),'25': ('Aybuke Abayli', 'Biyoloji'), '49':('Enes Sunbul', 'Cografya')}
	if ogrenci_no in ogr:
		html = '<b>Ogrencinin Adi:</b>%s <br/><b>Bolumu:</b>%s' % (ogr[ogrenci_no][0], ogr[ogrenci_no][1])
		return HttpResponse(html)
	else:
		raise Http404("Tanimli olmayan bir ogrenci ariyorsunuz")

def saat(request):
	return HttpResponse('Saat simdi: <b>%s</b>' % str(datetime.now()))
