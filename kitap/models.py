from django.db import models

# Create your models here.

class Tur(models.Model):
    adi = models.CharField(max_length=50)

    class Meta:
        ordering = ['adi']

    def __unicode__(self):
        return '%s' % self.adi
class Yazar(models.Model):
    adi = models.CharField(max_length=50)
    soyadi = models.CharField(max_length=50)
    telefonu = models.CharField(max_length=20)

    class Meta:
        ordering = ['soyadi']

    def __unicode__(self):
        return '%s, %s, %s' % (self.adi, self.soyadi, self.telefonu)

class Yayinevi(models.Model):
    adi = models.CharField(max_length=50)
    telefonu = models.CharField(max_length=20)
    adresi = models.CharField(max_length=75)

    class Meta:
        ordering = ['adi']

    def __unicode__(self):
        return '%s, %s, %s' % (self.adi, self.telefonu, self.adresi)

class Kitap(models.Model):
    turu = models.ForeignKey(Tur)
    adi = models.CharField(max_length=50)
    yazarlari = models.ManyToManyField(Yazar)
    yayinevi = models.ForeignKey(Yayinevi)

    class Meta:
        ordering = ['adi']

    def __unicode__(self):
        return '%s, %s, %s, %s' % (self.turu, self.adi, self.yazarlari, self.yayinevi)

