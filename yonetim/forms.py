from django import forms

class OgretimElemaniFormu(forms.Form):
    UNVANSECENEKLERI=(('AG', 'Arastirma Gorevlisi'), ('DR', 'Doktor'), ('YD', 'Yardimci Docent Doktor'), ('DD', 'Docent Doktor'), ('PD', 'Profesor Doktor'),)
    unvani = forms.ChoiceField(label="Unvani",
                             choices = UNVANSECENEKLERI, required=False)
    adi = forms.CharField(label="Adi")
    soyadi = forms.CharField(label="Soyadi")
    telefonu = forms.CharField(label="Telefon Numarasi",required=False)
    e_post_adresi = forms.EmailField(label="E-Posta Adresi",required=False)

    def clean_e_post_adresi(self):
        adres = self.cleaned_data['e_post_adresi']
        if '@' in adres:
            (kullanici, alan) = adres.split('@')
            if kullanici in ('root', 'admin', 'administrator'):
                raise forms.ValidationError('Bu adres gecersizdir!')
        return adres

class AramaFormu(forms.Form):
    aranacak_kelime=forms.CharField()

    def clean_aranacak_kelime(self):
        kelime = self.cleaned_data['aranacak_kelime']
        if len(kelime) < 3:
            raise forms.ValidationError('Aranacak kelime 3 harften az olamaz!')
        return kelime