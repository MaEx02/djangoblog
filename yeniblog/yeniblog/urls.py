from django.conf.urls import include, url
from django.contrib import admin
from blogSitesi import views
from django.urls import path
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('',views.anasayfa),
    path('post/<str:pk>/',views.gonderi_getir),
    path('posts/', views.gonderi_listesi),
]