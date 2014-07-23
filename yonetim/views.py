from django.template import RequestContext
from django.http import *
from models import *
from django.shortcuts import render_to_response
from yonetim.forms import *
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.


def ogretim_elemanlari_listesi(request):
    siralama = 'soyadi'
    olcut = request.GET.get('sirala')
    sayfa = request.GET.get('sayfa',1)
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
        except:
            return HttpResponse('Aradiginiz ogretim elemani bulunamiyor: ID=%s' % ogrElmID)

    if request.GET.get('sil'):
        ogrelm.delete()
        return HttpResponseRedirect('/ogretim-elemanlari-listesi/')

    if request.method == 'POST':
        form = OgretimElemaniFormu(request.POST)

        if form.is_valid():
            temiz_veri = form.cleaned_data
            if not ogrElmID: ogrelm=OgretimElemani()
            ogrelm.unvani = temiz_veri['unvani']
            ogrelm.adi = temiz_veri['adi']
            ogrelm.soyadi=temiz_veri['soyadi']
            ogrelm.telefonu=temiz_veri.get('telefonu')
            ogrelm.e_post_adresi=temiz_veri.get('e_post_adresi')
            ogrelm.save()
            return HttpResponseRedirect('/ogretim-elemanlari-listesi')
    else:
        if ogrElmID: form = OgretimElemaniFormu(initial=ogrelm.__dict__)
        else: form=OgretimElemaniFormu()
    return render_to_response(
                'genel_form.html',
                {'form':form, 'baslik':'Ogretim Elemani Ekleme', 'ID':ogrElmID},
                context_instance = RequestContext(request))
