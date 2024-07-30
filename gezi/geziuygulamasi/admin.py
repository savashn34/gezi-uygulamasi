from django.contrib import admin
from .models import Cinsiyetler, Uyruklar, Yerler, Lokantalar, Etkinlikler, Geziciler, Geziler, Gezginler, Odeme_Yontemleri, Diller, Yakinliklar, Doviz, Takimlar, Ucaklar, Ucus_Alanlari, Konaklamalar, Araclar, Etkinlik_Ayrintilari, Gezginler_Odeme

# Register your models here.

TURKCE_AYLAR = [
    'Ocak',
    'Şubat',
    'Mart',
    'Nisan',
    'Mayıs',
    'Haziran',
    'Temmuz',
    'Ağustos',
    'Eylül',
    'Ekim',
    'Kasım',
    'Aralık',
]

class MonthFilter(admin.SimpleListFilter):
    title = 'Ay'
    parameter_name = 'month'

    def lookups(self, request, model_admin):
        months = Takimlar.objects.dates('baslangic', 'month')
        sorted_months = sorted(months, key=lambda d: d.month)
        return [(month.month, TURKCE_AYLAR[month.month - 1]) for month in sorted_months]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(baslangic__month=self.value())

class YearFilter(admin.SimpleListFilter):
    title = 'Yıl'
    parameter_name = 'year'

    def lookups(self, request, model_admin):
        years = Takimlar.objects.dates('baslangic', 'year')
        return [(year.year, str(year.year)) for year in years]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(baslangic__year=self.value())

class TakimlarAdmin(admin.ModelAdmin):
    list_display = ("takim_adi", "gezi", "gezicisi", "baslangic",)
    search_fields = ("takim_adi",)
    list_filter = ("gezi", "gezicisi", "baslangic", YearFilter, MonthFilter)

class GezicilerAdmin(admin.ModelAdmin):
    search_fields = ("ad".title, "soyad".title,)
    list_filter = ("ad", "soyad", "dil",)

class GezginlerAdmin(admin.ModelAdmin):
    list_display = ("ad", "soyad", "pasaport_no",)
    search_fields = ("pasaport_no", "ad", "soyad",)

class Gezginler_OdemeAdmin(admin.ModelAdmin):
    list_display = ("gezgin", "gezgin_pasaport_no", "takim", "odendi",)
    search_fields = ("gezgin", "gezgin_pasaport_no", "takim",)
    list_filter = ("odendi", "odeme_yontemi", "doviz", "takim",)

    def gezgin_pasaport_no(self, obj):
        return obj.gezgin.pasaport_no
    
    gezgin_pasaport_no.short_description = 'Pasaport No'


admin.site.register(Cinsiyetler)
admin.site.register(Uyruklar)
admin.site.register(Yerler)
admin.site.register(Lokantalar)
admin.site.register(Etkinlikler)
admin.site.register(Geziciler, GezicilerAdmin)
admin.site.register(Geziler)
admin.site.register(Takimlar, TakimlarAdmin)
admin.site.register(Gezginler, GezginlerAdmin)
admin.site.register(Odeme_Yontemleri)
admin.site.register(Diller)
admin.site.register(Yakinliklar)
admin.site.register(Doviz)
admin.site.register(Ucaklar)
admin.site.register(Ucus_Alanlari)
admin.site.register(Konaklamalar)
admin.site.register(Araclar)
admin.site.register(Etkinlik_Ayrintilari)
admin.site.register(Gezginler_Odeme, Gezginler_OdemeAdmin)