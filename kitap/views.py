from django.shortcuts import render_to_response
from models import *
# Create your views here.

def yazarlar(request):
    yazarlar = Yazar.objects.all()
    return render_to_response('yazarlar_listesi.html', locals())

def kitaplar(request, no):
    kitaplar = Kitap.objects.filter(yazarlari = no)
    return render_to_response('kitap_listesi.html', locals())
