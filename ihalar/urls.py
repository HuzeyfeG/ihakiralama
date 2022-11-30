from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

#İhalar modülü için path'leri belirtiyoruz.
#Her görünüm için 'name' parametresi belirtip uygulama içinde kullanabiliyoruz.

urlpatterns = [
    path("main", views.index, name="main"),
    path("detail/<int:id>", views.ihaDetail, name="detail"),
    path("newad", views.newAdReq, name="newad"),
    path("myads", views.myAdsReq, name="myads"),
    path("edit/<int:id>", views.editReq, name="edit"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)