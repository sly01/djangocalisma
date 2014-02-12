# -*- coding: utf-8 -*-

from django.http import *
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
		return HttpResponse('<b>%s</b> kodlu bir ders yok' % ders_kodu)
	else:
		html=u'<b>%s</b> kodlu dersin adi <b>%s</b>, icerigi sonra gelecek.' % (ders_kodu,dersler[ders_kodu])
		return HttpResponse(html)