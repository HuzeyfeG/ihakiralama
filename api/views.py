from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from ihalar.models import Iha
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
import uuid


# Yapılacak 'POST' request'ler için oluşturduğumuz pathlere gelen request'lerin hangi işlemlere tabi tutulacağını burada
# fonksiyonlar tanımlıyoruz.
# Fonsksiyonları methodlarını @app_view modülü ile belirtiyoruz. 


@api_view(["POST"])
def signup(request):
    if request.path == "/api/signup": # Yapılan request sonrası tekrar requeset yapılma ihtimaline karşı path'i düzeltiyoruz.
        request.path = "/signup"
    username = request.POST['username']
    email = request.POST['email']
    password= request.POST['password'] # Request verilerini çekiyoruz.
    if User.objects.filter(username=username).exists():# Kullanıcı adının daha önce kullanılıp kullanılmadığını kontrol ediyoruz.
        return render(request, "signup.html", {"error": "Kullanıcı adı kullanılıyor!"})
    elif User.objects.filter(email=email).exists(): # Emailin daha önce kullanılıp kullanılmadığını kontrol ediyoruz. 
        return render(request, "signup.html", {"error": "E-mail kullanılıyor!"})
    else:
        user = User.objects.create_user(username=username, email=email, password=password) 
        user.save()  #Hata alınmaması durumunda  modeli oluşturup database'e kaydediyoruz.
        return render(request, "signup.html", {"message": "Kayıt Başarılı!"})


@api_view(["POST"])
def loginR(request):
    if request.path == "/api/login": # Yapılan request sonrası tekrar requeset yapılma ihtimaline karşı path'i düzeltiyoruz.
        request.path = "/login"
    username = request.POST['username']
    password= request.POST['password']# Request verilerini çekiyoruz.
    user = authenticate(request, username=username, password=password) # Kullanıcını varlığını kontrol ediyoruz.
    if user is not None:
        login(request, user) # Kullanıcı varsa giriş yaptırıyoruz.
        return redirect("main")
    else:
        return render(request, "login.html", {"error": "Kullanıcı ya da parola yanlış."})

@api_view(["POST"])
def index(request):
    if request.path == "/api/main": # Yapılan request sonrası tekrar requeset yapılma ihtimaline karşı path'i düzeltiyoruz.
        request.path = "/main"
    if request.POST["search"] == "filter":
        filtered = []
        armedFilter = request.POST["armedFilter"]
        altitudeFilter = request.POST["altitudeFilter"]
        weightFilter = request.POST["weightFilter"]
        flightTimeFilter = request.POST["flightTimeFilter"]# Request verilerini çekiyoruz.
        for filt in Iha.objects.all().filter(armed= True if armedFilter == "yes" else False):
            if int(filt.altitude) <= int(altitudeFilter) and int(filt.maxWeight) <= int(weightFilter) and int(filt.flightTime) <= int(flightTimeFilter):
                filtered.append(filt) # Filtreleme işlemleri için parametreleri düzenleyip sayfaya aktarımını yapıyoruz.
        return render(request, "index.html", {"ihaList": filtered})
    else:
        word = request.POST["searchBar"].capitalize()
        return render(request, "index.html", {"ihaList": Iha.objects.all().filter(Q(name=word) | Q(brand=word))})

@api_view(["POST"])
def ihaDetail(request, id):
    if request.path == "/api/detail/" + str(id): # Yapılan request sonrası tekrar requeset yapılma ihtimaline karşı path'i düzeltiyoruz.
        request.path = "/detal/" + str(id)
    iha = Iha.objects.get(id=id) # Detay sayfasında görülecek olarak objeyi databaseden çekiyoruz.
    if request.user.username != iha.owner:
        return render(request, "detail.html", {"iha": Iha.objects.get(id=id), "message": "İha başarı ile kiralandı."})
    else:
        return render(request, "detail.html", {"iha": Iha.objects.get(id=id), "error": "Kendi İha'na başvuru yapamazsın."})
    # Yaptığımız kontrol sonrası iha, giriş yapan kullanıcıya ait değilse kiralama işlemini gerçekleştiriyoruz yoksa hata döndürüyoruz.

@api_view(["POST"])
def newAdReq(request):
    if request.path == "/api/newad/": # Yapılan request sonrası tekrar requeset yapılma ihtimaline karşı path'i düzeltiyoruz.
        request.path = "/newad"
    name = request.POST['name']
    brand = request.POST['brand']
    description = request.POST['description']
    maxWeight = request.POST['maxWeight']
    flightTime = request.POST['flightTime']
    altitude = request.POST['altitude']
    ihaImage = request.FILES['ihaImage']
    armed = request.POST['armed']# Request verilerini çekiyoruz.
    if ihaImage.name.endswith(".jpg") or ihaImage.name.endswith(".jpeg") or ihaImage.name.endswith(".png"): # Dosya uzantısını kontrol ediyoruz. Başarılı ise devam ediyoruz değilse hata döndürüyoruz.
        fs = FileSystemStorage()
        ihaName = fs.url(str(uuid.uuid1()))
        fs.save(ihaName, ihaImage) # iha fotoğrafına belirtilen path'e ouşturulan id ile kaydediyoruz. Database'de fotoğraf path'ini saklıyoruzç
        Iha.objects.create(name=name, brand=brand, description=description, maxWeight=maxWeight, flightTime=flightTime, altitude=altitude, image=ihaName, armed= True if armed == "yes" else False, owner=request.user.username) # Modele uygun olan ihayı database'e kaydediyoruz.
        ihas = Iha.objects.all().filter(owner=request.user.username)
        return render(request, "myads.html", {"myAds": ihas}) # Kullanıcı yeni iha ilanının verdikten sonra 'ilanlarım' adresine yönlendiriyoruz.
    else:
        return render(request, "newad.html", {"error": "Lütfen '.jpeg', '.jpg' ya da '.png' uzantılı dosya ekleyiniz."})


@api_view(["POST"])
def editReq(request, id):
    if request.path == "/api/edit/" + str(id): # Yapılan request sonrası tekrar requeset yapılma ihtimaline karşı path'i düzeltiyoruz.
        request.path = "/edit/" + str(id)
    if request.POST["submit"] == "edit": # Kullanıcının hangi işlemi yapacağını  kontrol ediyoruz
        name = request.POST['name']
        brand = request.POST['brand']
        description = request.POST['description']
        maxWeight = request.POST['maxWeight']
        flightTime = request.POST['flightTime']
        altitude = request.POST['altitude']
        armed = request.POST['armed']# Request verilerini çekiyoruz.
        iha = Iha.objects.get(id=id)
        iha.name = name
        iha.brand = brand
        iha.description = description
        iha.maxWeight = maxWeight
        iha.flightTime = flightTime
        iha.altitude = altitude
        iha.armed = True if armed == "yes" else False
        iha.save() # Değiştirilen verileri modele kaydedip database'e tekrar yüklüyoruz.
        return redirect("myads")
    else:
        iha = Iha.objects.get(id=id)
        iha.delete() # İha verisini siliyoruz.
        return redirect("myads")
