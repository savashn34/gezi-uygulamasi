from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import TakimlarFilter
from datetime import datetime, timezone
from django_user_agents.utils import get_user_agent
from geziuygulamasi.models import Cinsiyetler, Uyruklar, Yerler, Lokantalar, Etkinlikler, Geziciler, Geziler, Gezginler, Odeme_Yontemleri, Diller, Yakinliklar, Doviz, Takimlar, Ucaklar, Ucus_Alanlari, Konaklamalar, Araclar, Etkinlik_Ayrintilari, Gezginler_Odeme

def index(request):
    if not request.user.is_authenticated:
        return redirect("giris")
    
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        user_id = request.GET.get('user_id')
        gezici = request.GET.get('gezici')
        geziler = request.GET.get('geziler')
        gelecek = request.GET.get('gelecek')
        gecmis = request.GET.get('gecmis')

        if request.user.is_superuser:
            documents = Takimlar.objects.all()
        else:
            gezici = Geziciler.objects.get(slug=request.user.username)
            documents = Takimlar.objects.filter(gezicisi=gezici)

        if start_date:
            documents = documents.filter(baslangic__gte=start_date)
        if end_date:
            documents = documents.filter(baslangic__lte=end_date)
        if user_id:
            documents = documents.filter(user_id=user_id)
        if gezici:
            documents = documents.filter(gezicisi=gezici)
        if geziler:
            documents = documents.filter(gezi=geziler)
        if gelecek:
            documents = documents.filter(baslangic__gt=datetime.now(timezone.utc))
        if gecmis:
            documents = documents.filter(baslangic__lt=datetime.now(timezone.utc))

        if not (start_date or end_date or user_id or gezici or geziler or gelecek or gecmis):
            documents = Takimlar.objects.all()

        q = request.GET.get('q')
        if q:
            if request.user.is_superuser:
                documents = documents.filter(takim_adi__icontains=q)
            else:
                documents = documents.filter(takim_adi__icontains=q, gezicisi=gezici)

        content_per_page = 20
        paginator = Paginator(documents, content_per_page)
        page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    bugun = datetime.now()
    bugunku_etkinlikler = Takimlar.objects.filter(baslangic__year=bugun.year, baslangic__month=bugun.month, baslangic__day=bugun.day)
    user_agent = get_user_agent(request)
    context = {
        "geziciler": Geziciler.objects.all(),
        "geziler": Geziler.objects.all(),
        "diller": Diller.objects.all(),
        "bugunku_etkinlikler": bugunku_etkinlikler,
        "documents": documents,
        "page_obj": page_obj,
        "user_agent": user_agent,
    }
    return render(request, "index.html", context)

def geziler(request):
    if not request.user.is_authenticated:
        return redirect("giris")
    user_agent = get_user_agent(request)
    context = {
        "geziler": Geziler.objects.all(),
        "takimlar": Takimlar.objects.all(),
        "user_agent": user_agent,
    }
    return render(request, 'geziler.html', context)

def geziciler(request):
    if not request.user.is_authenticated:
        return redirect("giris")
    user_agent = get_user_agent(request)
    context = {
        "geziciler": Geziciler.objects.all(),
        "user_agent": user_agent,
    }
    return render(request, "geziciler.html", context)

def gezici(request, slug):
    if not request.user.is_authenticated:
        return redirect("giris")
    gezici = Geziciler.objects.filter(slug=slug)
    takimlar = Takimlar.objects.filter(gezicisi__slug=slug)
    user_agent = get_user_agent(request)
    context = {
        "geziciler": Geziciler.objects.get(slug=slug),
        "geziler": Geziler.objects.all(),
        "diller": Diller.objects.all(),
        "takimlar": takimlar,
        "gezici": gezici,
        "user_agent": user_agent,
    }
    return render(request, "gezici.html", context)

def takimlar(request):
    if not request.user.is_authenticated:
        return redirect("giris")
    takimlar = Takimlar.objects.all()

    q = request.GET.get('q')
    if q:
        takimlar = takimlar.filter(takim_adi__icontains=q)

    content_per_page = 20
    paginator = Paginator(takimlar, content_per_page)
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    user_agent = get_user_agent(request)
    context = {
        "page_obj": page_obj,
        "user_agent": user_agent,
    }
    return render(request, "takimlar.html", context)

def takim(request, slug):
    takim = Takimlar.objects.filter(slug=slug)
    user_agent = get_user_agent(request)
    context = {
        "takim": takim,
        "etkinlikler": Etkinlik_Ayrintilari.objects.filter(takim__slug=slug),
        "gezginler": Gezginler.objects.filter(takim__slug=slug),
        "user_agent": user_agent,
    }
    return render(request, "takim.html", context)

def gecmis(request):
    if not request.user.is_authenticated:
        return redirect("giris")
    
    bugun = datetime.now()
    baslangic_min = request.GET.get('baslangic_min', '')
    baslangic_max = request.GET.get('baslangic_max', '')

    if request.user.is_superuser:
        gecmis_etkinlikler = Takimlar.objects.filter(baslangic__lt=bugun)
        filter = TakimlarFilter(request.GET, queryset=gecmis_etkinlikler)
    else:
        gezici = Geziciler.objects.get(slug=request.user.username)
        gecmis_etkinlikler = Takimlar.objects.filter(baslangic__lt=bugun, gezicisi=gezici)
        filter = TakimlarFilter(request.GET, queryset=gecmis_etkinlikler)

    user_agent = get_user_agent(request)
    context = {
        "bugun": bugun,
        "filter": filter,
        "baslangic_min": baslangic_min,
        "baslangic_max": baslangic_max,
        "user_agent": user_agent,
    }
    return render(request, 'gecmis.html', context)

def gelecek(request):
    if not request.user.is_authenticated:
        return redirect("giris")
    bugun = datetime.now()
    baslangic_min = request.GET.get('baslangic_min', '')
    baslangic_max = request.GET.get('baslangic_max', '')
    if request.user.is_superuser:
        gelecek_etkinlikler = Takimlar.objects.filter(baslangic__gt=bugun)
        filter = TakimlarFilter(request.GET, queryset=Takimlar.objects.filter(baslangic__gt=bugun))
    else:
        gezici = Geziciler.objects.get(slug=request.user.username)
        gelecek_etkinlikler = Takimlar.objects.filter(baslangic__gt=bugun, gezicisi=gezici)
        filter = TakimlarFilter(request.GET, queryset=Takimlar.objects.filter(baslangic__gt=bugun, gezicisi=gezici))

    user_agent = get_user_agent(request)
    context = {
        "bugun": bugun,
        "gelecek_etkinlikler": gelecek_etkinlikler,
        "filter": filter,
        "baslangic_min": baslangic_min,
        "baslangic_max": baslangic_max,
        "user_agent": user_agent,
    }
    return render(request, 'gelecek.html', context)

def gezgin(request, slug):
    if not request.user.is_authenticated:
        return redirect("giris")
    gezgin = Gezginler.objects.filter(slug=slug)
    gezgin_odeme = Gezginler_Odeme.objects.filter(gezgin__slug=slug)
    user_agent = get_user_agent(request)
    context = {
        "gezgin": gezgin,
        "gezgin_odeme": gezgin_odeme,
        "user_agent": user_agent,
    }
    return render(request, 'gezgin.html', context)

def gezginler(request):
    if not request.user.is_authenticated:
        return redirect("giris")
    
    if request.method == 'GET':
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')
        takim = request.GET.get('takim')
        odeme = request.GET.get('odeme')
        gezi = request.GET.get('gezi')
        ad = request.GET.get('ad')
        soyad = request.GET.get('soyad')
        uyruk = request.GET.get('uyruk')

        gezginler = Gezginler.objects.all()
        geziler = Geziler.objects.all()
        odeme_yontemi = Odeme_Yontemleri.objects.all()
        gezginler_odeme = Gezginler_Odeme.objects.all()
        takimlar = Takimlar.objects.all()
        uyruklar = Uyruklar.objects.all()

        if start_date:
            gezginler = gezginler.filter(takim__baslangic__gte=start_date)
        if end_date:
            gezginler = gezginler.filter(takim__bitis__lte=end_date)
        if takim:
            gezginler = gezginler.filter(takim__takim_adi=takim)
        if odeme:
            gezginler = gezginler.filter(gezginler_odeme__odendi=odeme)
        if gezi:
            gezginler = gezginler.filter(takim__gezi__gezi=gezi)
        if ad:
            gezginler = gezginler.filter(ad=ad)
        if soyad:
            gezginler = gezginler.filter(soyad=soyad)
        if uyruk:
            gezginler = gezginler.filter(uyruk__uyruk=uyruk)

        if not (start_date or end_date or takim or odeme or gezi or ad or soyad or uyruk):
            gezginler = Gezginler.objects.all()

        q = request.GET.get('q')
        if q:
            gezginler = gezginler.filter(pasaport_no__icontains=q)

    content_per_page = 20
    paginator = Paginator(gezginler, content_per_page)
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    user_agent = get_user_agent(request)
    context = {
        "gezginler": gezginler,
        "geziler": geziler,
        "odeme_yontemi": odeme_yontemi,
        "gezginler_odeme": gezginler_odeme,
        "takimlar": takimlar,
        "uyruklar": uyruklar,
        "page_obj": page_obj,
        "user_agent": user_agent,
    }
    return render(request, 'gezginler.html', context)