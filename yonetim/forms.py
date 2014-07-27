from django.forms import ModelForm
from django import forms
from models import *
from django.forms import Textarea
class OgretimElemaniFormu(ModelForm):
    class Meta:
        model = OgretimElemani

    def clean_e_post_adresi(self):
        adres = self.cleaned_data['e_post_adresi']
        if '@' in adres:
            (kullanici, alan) = adres.split('@')
            if kullanici in ('root', 'admin', 'administrator'):
                raise forms.ValidationError('Bu adres gecersizdir!')
        return adres

class DersFormu(ModelForm):
    class Meta:
        model=Ders
        widgets = {
            'tanimi': Textarea(attrs={'cols':35, 'rows': 5}),
        }

class OgretimElemaniAltFromu(ModelForm):
    class Meta:
        model = OgretimElemani
        fields = ('adi', 'soyadi', 'e_post_adresi')



class AramaFormu(forms.Form):
    aranacak_kelime=forms.CharField()

    def clean_aranacak_kelime(self):
        kelime = self.cleaned_data['aranacak_kelime']
        if len(kelime) < 3:
            raise forms.ValidationError('Aranacak kelime 3 harften az olamaz!')
        return kelime

