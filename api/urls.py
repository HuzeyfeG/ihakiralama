from django.urls import path
from . import views


# Yapılacak 'POST' request'ler için kullanacağımız pathleri belirtiyoruz.

urlpatterns = [
    path("signup", views.signup),
    path("login", views.loginR),
    path("main", views.index),
    path("detail/<int:id>", views.ihaDetail),
    path("newad", views.newAdReq),
    path("edit/<int:id>", views.editReq),
]