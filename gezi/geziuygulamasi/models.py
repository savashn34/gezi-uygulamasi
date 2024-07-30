from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

# Create your models here.

class Ucaklar(models.Model):
    ucak = models.CharField(max_length=50)

    def __str__(self):
        return self.ucak
    
class Ucus_Alanlari(models.Model):
    ucus_alani = models.CharField(max_length=100)

    def __str__(self):
        return self.ucus_alani

class Doviz(models.Model):
    doviz = models.CharField(max_length=10)

    def __str__(self):
        return self.doviz

class Yakinliklar(models.Model):
    yakinlik = models.CharField(max_length=50)

    def __str__(self):
        return self.yakinlik

class Cinsiyetler(models.Model):
    cinsiyet = models.CharField(max_length=50)

    def __str__(self):
        return self.cinsiyet

class Uyruklar(models.Model):
    uyruk = models.CharField(max_length=100)

    def __str__(self):
        return self.uyruk
    
class Yerler(models.Model):
    yer = models.CharField(max_length=200)

    def __str__(self):
        return self.yer
    
class Lokantalar(models.Model):
    lokanta = models.CharField(max_length=200)
    il = models.CharField(max_length=100)
    ilçe = models.CharField(max_length=100)
    konum = models.CharField(max_length=500)
    lokanta_iletisim = models.CharField(max_length=50)
    yetkilisi = models.CharField(max_length=100)
    yetkili_iletisim = models.CharField(max_length=50)

    def __str__(self):
        return self.lokanta
    
class Konaklamalar(models.Model):
    konaklama = models.CharField(max_length=200)
    il = models.CharField(max_length=100)
    ilçe = models.CharField(max_length=100)
    konum = models.CharField(max_length=500)
    konaklama_iletisim = models.CharField(max_length=50)
    yetkilisi = models.CharField(max_length=100)
    yetkili_iletisim = models.CharField(max_length=50)

    def __str__(self):
        return self.konaklama
    
class Araclar(models.Model):
    kurulus = models.CharField(max_length=200)
    kurulus_iletisim = models.CharField(max_length=50)
    yetkilisi = models.CharField(max_length=100)
    yetkili_iletisim = models.CharField(max_length=50)

    def __str__(self):
        return self.kurulus
    
class Diller(models.Model):
    dil = models.CharField(max_length=50)
    
    def __str__(self):
        return self.dil

class Geziciler(models.Model):
    ad = models.CharField(max_length=100)
    gobek_adi = models.CharField(max_length=100, null=True, blank=True)
    soyad = models.CharField(max_length=100)
    dil = models.ManyToManyField(Diller)
    cinsiyet = models.ForeignKey(Cinsiyetler, on_delete=models.CASCADE)
    dogum = models.DateField()
    uyruk = models.ForeignKey(Uyruklar, on_delete=models.CASCADE)
    kimlik_no = models.CharField(max_length=100)
    e_posta = models.CharField(max_length=100)
    telefon = models.CharField(max_length=50)
    yakin_ad = models.CharField(max_length=100)
    yakinlik = models.ForeignKey(Yakinliklar, on_delete=models.CASCADE)
    yakin_tel = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True)

    def __str__(self):
        return f"{self.ad} {self.soyad}"
    
    def save(self, *args, **kwargs):
        combined_name = f"{self.ad}{self.soyad}"
        slug_text = unidecode(combined_name)
        self.slug = slugify(slug_text)
        super().save(*args, **kwargs)
    
class Geziler(models.Model):
    gezi = models.CharField(max_length=250)
    gun_sayisi = models.IntegerField(default=0)
    gece_sayisi = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.gezi} {self.gun_sayisi} gün {self.gece_sayisi} gece"

class Takimlar(models.Model):
    takim_adi = models.CharField(max_length=50, null=True)
    gezi = models.ForeignKey(Geziler, on_delete=models.CASCADE)
    baslangic = models.DateTimeField(null=False)
    bitis = models.DateTimeField(null=False)
    gezicisi = models.ForeignKey(Geziciler, on_delete=models.CASCADE)
    gidis_ucagi = models.ForeignKey(Ucaklar, related_name='gidis_ucagi', on_delete=models.CASCADE)
    gidis_ucus_no = models.CharField(max_length=50)
    gidis_ucak_kalkis_yeri = models.ForeignKey(Ucus_Alanlari, null=True, related_name='gidis_ucak_kalkis_yeri', on_delete=models.CASCADE)
    gidis_ucak_kalkis = models.DateTimeField(null=True)
    gidis_ucak_inis_yeri = models.ForeignKey(Ucus_Alanlari, null=True, related_name='gidis_ucak_inis_yeri', on_delete=models.CASCADE)
    gidis_ucak_inis = models.DateTimeField(null=True)
    donus_ucagi = models.ForeignKey(Ucaklar, null=True, related_name='donus_ucagi', on_delete=models.CASCADE)
    donus_ucus_no = models.CharField(max_length=50)
    donus_ucak_kalkis_yeri = models.ForeignKey(Ucus_Alanlari, null=True, related_name='donus_ucak_kalkis_yeri', on_delete=models.CASCADE)
    donus_ucak_kalkis = models.DateTimeField(null=True)
    donus_ucak_inis_yeri = models.ForeignKey(Ucus_Alanlari, null=True, related_name='donus_ucak_inis_yeri', on_delete=models.CASCADE)
    donus_ucak_inis = models.DateTimeField(null=True)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True)

    def __str__(self):
        return self.takim_adi
    
    def save(self, *args, **kwargs):
        slug_text = unidecode(self.takim_adi)
        self.slug = slugify(slug_text)
        super().save(*args, **kwargs)
    
class Etkinlikler(models.Model):
    etkinlik_adi = models.CharField(max_length=200) ## KONAKLAMA, YEMEK YEME, YOLCULUK, GEZİNTİ GİBİ GİBİ

    def __str__(self):
        return self.etkinlik_adi
    
class Etkinlik_Ayrintilari(models.Model):
    takim = models.ForeignKey(Takimlar, on_delete=models.CASCADE)
    etkinlik = models.ForeignKey(Etkinlikler, on_delete=models.CASCADE)
    etkinlik_suresi = models.DateTimeField()
    konaklama_yeri = models.ForeignKey(Konaklamalar, null=True, blank=True, on_delete=models.CASCADE)
    arac_plakasi = models.CharField(max_length=50, null=True, blank=True)
    arac_kurulusu = models.ForeignKey(Araclar, null=True, blank=True, on_delete=models.CASCADE)
    yemek_yeri = models.ForeignKey(Lokantalar, null=True, blank=True, on_delete=models.CASCADE)
    ucus_alani = models.ForeignKey(Ucus_Alanlari, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.takim.takim_adi)
    
class Odeme_Yontemleri(models.Model):
    odeme_yontemi = models.CharField(max_length=100)

    def __str__(self):
        return self.odeme_yontemi

class Gezginler(models.Model):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    cinsiyet = models.ForeignKey(Cinsiyetler, on_delete=models.CASCADE)
    dogum = models.DateField()
    uyruk = models.ForeignKey(Uyruklar, on_delete=models.CASCADE)
    pasaport_no = models.CharField(max_length=100)
    e_posta = models.CharField(max_length=100)
    telefon = models.CharField(max_length=50)
    adres = models.CharField(max_length=500)
    yakin_ad = models.CharField(max_length=100)
    yakinlik = models.ForeignKey(Yakinliklar, on_delete=models.CASCADE)
    yakin_tel = models.CharField(max_length=50)
    takim = models.ManyToManyField(Takimlar)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True)

    def __str__(self):
        return f"{self.ad} {self.soyad}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.pasaport_no)
        super().save(*args, **kwargs)

class Gezginler_Odeme(models.Model):
    takim = models.ForeignKey(Takimlar, on_delete=models.CASCADE, null=True, blank=True)
    gezgin = models.ForeignKey(Gezginler, on_delete=models.CASCADE)
    tutar = models.CharField(max_length=100)
    doviz = models.ForeignKey(Doviz, on_delete=models.CASCADE)
    odeme_yontemi = models.ForeignKey(Odeme_Yontemleri, on_delete=models.CASCADE)
    odendi = models.BooleanField(default=False)

    def __str__(self):
        return str(self.gezgin)
