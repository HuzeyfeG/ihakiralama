from django.shortcuts import render, redirect
from .models import Iha
from django.core.files.storage import FileSystemStorage
from django.db.models import Q

#Bu kısımda oluşturduğumuz view'leri fonksiyon olarak tanımlayıp görüntülüyoruz.

def index(request):
    if request.user.is_authenticated: # Kullanıcı giriş yapıp yapıp yapmadığını kontrol ediyoruz. Bu kontrolü yapabilmek için form içerindeki 'sessionid' yi kontol ediyoruz.
        return render(request, "index.html", {"ihaList": Iha.objects.all()}) # Anasayfada tüm ilanları database'den çekip gösteriyoruz.
    else:  
        return redirect("login")
    

def ihaDetail(request, id):
    if request.user.is_authenticated: # Kullanıcı giriş yapıp yapıp yapmadığını kontrol ediyoruz. Bu kontrolü yapabilmek için form içerindeki 'sessionid' yi kontol ediyoruz.
        return render(request, "detail.html", {"iha": Iha.objects.get(id=id)}) # İlanda seçilen ihayı database'den tüm özelliklerini çekerek gösteriyoruz.
    else:
        return redirect("login")

def newAdReq(request):
    if request.user.is_authenticated: # Kullanıcı giriş yapıp yapıp yapmadığını kontrol ediyoruz. Bu kontrolü yapabilmek için form içerindeki 'sessionid' yi kontol ediyoruz.
        return render(request, "newad.html") # Kulalnıcıyı yeni ilan sayfasına yönelendiriyoruz
    else:
        return redirect("login")

def myAdsReq(request):
    if request.user.is_authenticated: # Kullanıcı giriş yapıp yapıp yapmadığını kontrol ediyoruz. Bu kontrolü yapabilmek için form içerindeki 'sessionid' yi kontol ediyoruz.
        ihas = Iha.objects.all().filter(owner=request.user.username)
        return render(request, "myads.html", {"myAds": ihas}) # Kullanıcıyı kendi ilanalrını olduğumu sayfaya yönlendiriyoruz.
    else:
        return redirect("login")

def editReq(request, id):
    if request.user.is_authenticated: # Kullanıcı giriş yapıp yapıp yapmadığını kontrol ediyoruz. Bu kontrolü yapabilmek için form içerindeki 'sessionid' yi kontol ediyoruz.
        return render(request, "edit.html", {"iha": Iha.objects.get(id=id)}) # Kullanıcının ilanlarını güncelleyebileceği veya silebileceği sayfaya yönlendiriyoruz.
    else:
        return redirect("login")
