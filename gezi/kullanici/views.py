from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def giris_istegi(request):
    if request.user.is_authenticated:
        return redirect("baslangic")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("baslangic")
        else:
            return render(request, "kullanici/giris.html", {
                "error": "Yanlış kullanıcı adıyla şifre."
            })

    return render(request, "kullanici/giris.html")

def cikis_istegi(request):
    logout(request)
    return redirect("baslangic")