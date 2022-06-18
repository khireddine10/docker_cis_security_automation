"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('index', views.home, name="index"),
    path('hosts/<str:pk>/', views.hosts, name="hosts"),
    path('cischecks/<str:pk>/', views.cisChecks, name="cischecks"),
    path('vulchecks', views.vulChecks, name="vulchecks"),
    path('signin', views.login_view, name="signin"),
    path('logout', views.logout, name='logout'),
    path('addhost', views.addHost, name='addhost'),
    path('modifyhost', views.modifyHost, name='modifyhost'),
    path('deletehost', views.deleteHost, name='deletehost'),
    path('lastcheck/<str:pk>/', views.lastCheck, name="lastcheck"),
    path('runcheck', views.runCheck, name="runcheck"),
    path('checkcor/<str:pk>/', views.checkCor, name="checkcor"),
    path('addCor', views.addCor, name="addcor"),
    path('runcor', views.runCor, name="runcor")

]
