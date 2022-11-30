from django.urls import path
from . import views


#Users modülü için path'leri belirtiyoruz.
#Her görünüm için 'name' parametresi belirtip uygulama içinde kullanabiliyoruz.

urlpatterns = [
    path("", views.loginReq, name="login"),
    path("login", views.loginReq, name="login"),
    path("signup", views.signupReq, name="signup"),
    path("logout", views.logoutReq, name="logout")
]