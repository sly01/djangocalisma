from django.template import RequestContext
from django.http import *
from models import *
from django.shortcuts import render_to_response
from yonetim.forms import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms.models import modelformset_factory
import random
import time
from django.contrib.auth.decorators import login_required
# Create your views here.


def ogretim_elemanlari_listesi(request):
    if request.GET.get('sirala'):
        request.session['ogretim_elemani_siralama'] = request.GET['sirala']
    if not 'ogretim_elemani_siralama' in request.session:
        request.session['ogretim_elemani_siralama'] = '1'
    olcut = request.session['ogretim_elemani_siralama']
    if request.GET.get('sayfa'):
        request.session['ogretim_elemani_sayfa'] = request.GET['sayfa']
    if not 'ogretim_elemani_sayfa' in request.session:
        request.session['ogretim_elemani_sayfa'] = '1'
    sayfa = request.session['ogretim_elemani_sayfa']
    if olcut:
        siralamaOlcutleri = {
            '1':'adi',
            '2':'soyadi',
            '3':'e_post_adresi'
        }
        if olcut in siralamaOlcutleri:
            siralama = siralamaOlcutleri[olcut]
    ogretim_elemanlari_tumu = OgretimElemani.objects.order_by(siralama)

    arama_formu = AramaFormu()
    if request.GET.get('aranacak_kelime'):
        arama_formu = AramaFormu(request.GET)
        if arama_formu.is_valid():
            aranacak_kelime = arama_formu.cleaned_data['aranacak_kelime']
            ogretim_elemanlari_tumu = OgretimElemani.objects.filter(
                Q(adi__contains=aranacak_kelime) | Q(soyadi__contains=aranacak_kelime)
            )

    ogretim_elemanlari_sayfalari = Paginator(ogretim_elemanlari_tumu, 10)
    ogretim_elemanlari = ogretim_elemanlari_sayfalari.page(int(sayfa))
    for ogrelm in ogretim_elemanlari:
        verdigi_dersler = Ders.objects.filter(ogretim_elemani=ogrelm)
        ogrelm.verdigi_dersler=verdigi_dersler
    return render_to_response('ogretim_elemanlari_listesi.html', locals())

def get_deneme(request):
    if request.method == 'GET':
        adi = request.GET['adi']
        soyadi = request.GET['soyadi']
        return HttpResponse('<b>Adi:</b> %s <br><b>Soyadi:</b> %s' % (adi, soyadi))
def ogretim_elemani_ekleme(request):
    ogrElmID = request.GET.get('id')

    if ogrElmID:
        try:
            ogrelm = OgretimElemani.objects.get(id=ogrElmID)
            form = OgretimElemaniFormu(instance=ogrelm)
        except:
            return HttpResponse('Aradiginiz ogretim elemani bulunamiyor: ID=%s' % ogrElmID)

    else:
        form = OgretimElemaniFormu()

    if request.GET.get('sil'):
        ogrelm.delete()
        return HttpResponseRedirect('/ogretim-elemanlari-listesi/')

    if request.method == 'POST':
        if ogrElmID:
            form = OgretimElemaniFormu(request.POST, instance=ogrelm)
        else:
            form = OgretimElemaniFormu(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ogretim-elemanlari-listesi')
    else:
        if ogrElmID: form = OgretimElemaniFormu(initial=ogrelm.__dict__)
        else: form=OgretimElemaniFormu()
    return render_to_response(
                'genel_form.html',
                {'form':form, 'baslik':'Ogretim Elemani Ekleme', 'ID':ogrElmID},
                context_instance = RequestContext(request))

def coklu_ogretim_elemani_ekleme(request):
    OgretimElemaniFormuKumesi = modelformset_factory(OgretimElemani,
                                                     fields=('unvani', 'adi', 'soyadi'),
                                                     can_delete=True)
    if request.method == 'POST':
        formkumesi = OgretimElemaniFormuKumesi(request.POST)
        if formkumesi.is_valid():
            formkumesi.save()
            return HttpResponseRedirect('/coklu-ogretim-elemani-ekleme/')
    else:
        formkumesi = OgretimElemaniFormuKumesi()

    return render_to_response(
            'coklu_ogretim_elemani.html',
            locals(),
            context_instance=RequestContext(request))

def ders_listesi(request):
    siralama='adi'
    olcut = request.GET.get('sirala')
    sayfa = request.GET.get('sayfa',1)
    if olcut:
        siralamaOlcutleri = {
            '1':'kodu',
            '2':'adi',
            '3':'ogretim_elemani'
        }
        if olcut in siralamaOlcutleri:
            siralama = siralamaOlcutleri[olcut]
    ders_listesi_tumu = Ders.objects.order_by(siralama)

    ders_listesi_sayfalari = Paginator(ders_listesi_tumu,5)
    ders_listesi = ders_listesi_sayfalari.page(int(sayfa))

    return render_to_response('ders_listesi.html', locals())

def ders_ekleme(request):
    dersID = request.GET.get('id')

    if dersID:
        try:
            ders = Ders.objects.get(id=dersID)
            form = DersFormu(instance=ders)
        except:
            return HttpResponse('Aradiginiz ders bulunamiyor: ID=%s' % dersID)
    else:
        form = DersFormu()

    if request.GET.get('sil'):
        ders.delete()
        return HttpResponseRedirect('/ders-listesi')
    if request.method == 'POST':
        if dersID:
            form = DersFormu(request.POST, instance=ders)
        else:
            form = DersFormu(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ders-listesi')
    else:
        if dersID:
            form = DersFormu(initial=ders.__dict__)
        else:
            form = DersFormu()
    return render_to_response(
        'genel_form.html',
        {'form':form, 'baslik': 'Ders ekleme', 'ID':dersID},
        context_instance = RequestContext(request))

def ogrenci_listesi(request):
    siralama = 'adi'
    olcut = request.GET.get('sirala')
    sayfa = request.GET.get('sayfa',1)
    if olcut:
        siralamaOlcutleri = {
            '1':'numarasi',
            '2':'adi',
            '3':'soyadii'
        }
        if olcut in siralamaOlcutleri:
            siralama = siralamaOlcutleri[olcut]
    ogrenci_listesi_tumu = Ogrenci.objects.order_by(siralama)

    ogrenci_listesi_sayfalari = Paginator(ogrenci_listesi_tumu, 5)
    ogrenci_listesi = ogrenci_listesi_sayfalari.page(int(sayfa))

    return render_to_response('ogrenci_listesi.html', locals())

def ogrenci_ekleme(request):
    ogrID = request.GET.get('id')

    if ogrID:
        try:
            ogrenci = Ogrenci.objects.get(id=ogrID)
            form = OgrenciFormu(instance=ogrenci)
        except:
            return HttpResponse('Aradiginiz ogrenci bulunamiyor: ID=%s' % ogrID)
    else:
        form = OgrenciFormu()

    if request.GET.get('sil'):
        ogrenci.delete()
        return HttpResponseRedirect('/ogrenci-listesi')
    if request.method == 'POST':
        if ogrID:
            form = OgrenciFormu(request.POST, instance=ogrenci)
        else:
            form = OgrenciFormu(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ogrenci-listesi')
    else:
        if ogrID:
            form = OgrenciFormu(initial=ogrenci.__dict__)
        else:
            form = OgrenciFormu()
    return render_to_response(
        'genel_form.html',
        {'form':form, 'baslik': 'Ogrenci Ekleme', 'ID':ogrID},
        context_instance = RequestContext(request))
@login_required
def yonetim(request):
    return render_to_response('yonetim.html',locals())

def cerez_deneme(request):
    cerez_listesi = ['Findik', 'Fistik', 'Ceviz', 'Badem', 'Leblebi', 'Misir Kavurgasi']
    if not 'sevdigim_cerez' in request.COOKIES:
        sevdigim_cerez = random.choice(cerez_listesi)
        gun = 7
        son_kullanma_tarihi = time.strftime('%a, %d-%b-%Y %H:%M:S GMT', time.localtime(time.time() + gun*24*60*60))
        response = HttpResponse(
            'Sevidign cerez yoktu sana su cerezi sevdirdim: <b>%s</b>' % sevdigim_cerez
        )
        response.set_cookie('sevdigim_cerez', sevdigim_cerez, expires=son_kullanma_tarihi)
        return  response
    else:
        sevdigim_cerez = request.COOKIES['sevdigim_cerez']
        return HttpResponse(
            'Sevdigin cerez budur: <b>%s</b>' % sevdigim_cerez
        )