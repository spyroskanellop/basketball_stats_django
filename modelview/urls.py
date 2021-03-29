from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from run import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('team', views.team),
    path('conf', views.admin),
    path('home', views.home),
]
