from django.db import models

# Create your models here.
class OgretimElemani(models.Model):
    UNVANSECENEKLERI=(('AG', 'Arastirma Gorevlisi'), ('DR', 'Doktor'), ('YD', 'Yardimci Docent Doktor'), ('DD', 'Docent Doktor'), ('PD', 'Profesor Doktor'),)
    unvani = models.CharField(max_length=2, choices=UNVANSECENEKLERI, blank=True, verbose_name='Unvani')
    adi = models.CharField(max_length=50, verbose_name='Adi')
    soyadi = models.CharField(max_length=50, verbose_name='Soyadi')
    telefonu = models.CharField(max_length=50, blank=True, verbose_name='Telefon Numarasi')
    e_post_adresi = models.EmailField(blank=True, verbose_name='E-Posta Adresi')

    def __unicode__(self):
        return '%s, %s' % (self.soyadi, self.adi)

    class Meta:
        ordering = ['soyadi']

class Ders(models.Model):
    kodu = models.CharField(max_length=10)
    adi = models.CharField(max_length=50)
    ogretim_elemani = models.ForeignKey(OgretimElemani)
    tanimi = models.CharField(max_length=1000, blank=True)


    def __unicode__(self):
        return 'Ders: %s: %s' % (self.kodu, self.adi)
    class Meta:
        ordering = ['kodu']

class Ogrenci(models.Model):
    numarasi = models.IntegerField()
    adi = models.CharField(max_length=50)
    soyadi = models.CharField(max_length=50)
    aldigi_dersler = models.ManyToManyField(Ders)
    cinsiyet = models.CharField(max_length=1)

    def __unicode__(self):
        return 'Ogrenci: %s, %s' % (self.soyadi, self.adi)

    class Meta:
        ordering = ['soyadi']
