from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


#Bu kısımda oluşturduğumuz view'leri fonksiyon olarak tanımlayıp görüntülüyoruz.

def signupReq(request):
    if request.user.is_authenticated: # Kullanıcı giriş yapıp yapıp yapmadığını kontrol ediyoruz. Bu kontrolü yapabilmek için form içerindeki 'sessionid' yi kontol ediyoruz.
        return redirect("main") # Yaptıysa anasayfaya yapmadıysa üye olma kısmına yönlendiriyoruz.
    return render(request, "signup.html")

def loginReq(request):
    if request.user.is_authenticated: # Kullanıcı giriş yapıp yapıp yapmadığını kontrol ediyoruz. Bu kontrolü yapabilmek için form içerindeki 'sessionid' yi kontol ediyoruz.
        return redirect("main") # Yaptıysa anasayfaya yapmadıysa üye olma kısmına yönlendiriyoruz.
    return render(request, "login.html")

def logoutReq(request):
    logout(request) # Kullanıcıya uygulamadan çıkış yaptırıyoruz.
    return redirect("login")