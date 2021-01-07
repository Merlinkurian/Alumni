"""alumni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from alumniapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login', views.login, name='index'),
    path('registration', views.registration, name='registration'),
    path('getnames', views.getnames, name='getnames'),


    path('adminhome', views.adminhome, name='adminhome'),
    path('adminbatch', views.adminbatch, name='adminbatch'),
    path('adminalumni', views.adminalumni, name='adminalumni'),
    path('adminupdatealumni', views.adminupdatealumni, name='adminupdatealumni'),
    path('adminevent', views.adminevent, name='adminevent'),
    path('adminemanager', views.adminemanager, name='adminemanager'),


    path('emhome', views.emhome, name='emhome'),
    path('emchangepwd', views.emchangepwd, name='emchangepwd'),
    path('emgallery', views.emgallery, name='emgallery'),
    path('emevent', views.emevent, name='emevent'),
    path('emeventdelete', views.emeventdelete, name='emeventdelete'),


    path('alumnihome', views.alumnihome, name='alumnihome'),
    path('alumniprofile', views.alumniprofile, name='alumniprofile'),
    path('alumnievent', views.alumnievent, name='alumnievent'),
    path('alumnieventpgm', views.alumnieventpgm, name='alumnieventpgm'),
    path('alumnivaccancy', views.alumnivaccancy, name='alumnivaccancy'),
    path('alumniovaccancy', views.alumniovaccancy, name='alumniovaccancy'),
    path('alumnichat', views.alumnichat, name='alumnichat'),
    path('eventregistration', views.eventregistration, name='eventregistration'),
    path('alumnipayment', views.alumnipayment, name='alumnipayment'),
    path('selecteventregistration', views.selecteventregistration, name='selecteventregistration'),
    path('batchreport', views.batchreport, name='batchreport'),
    path('alumnireport', views.alumnireport, name='alumnireport'),
    path('unregisteredreport', views.unregisteredreport, name='unregisteredreport'),
    path('eventreport', views.eventreport, name='eventreport'),
    path('meetreport', views.meetreport, name='meetreport'),
    path('alumnibatchview', views.alumnibatchview, name='alumnibatchview'),
    path('adminupdateevent', views.adminupdateevent, name='adminupdateevent'),
    path('admindeleteevent', views.admindeleteevent, name='admindeleteevent'),
    
    
]
