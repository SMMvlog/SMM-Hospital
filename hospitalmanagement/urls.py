"""hospitalmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('log/', views.log,name="log"),
    path('contact/', views.contact,name="contact"),
    path('logt/', views.logOut,name="logt"),
    path('about/', views.about,name="about"),
    path('viewdoc/', views.viewdoc,name="viewdoc"),
    path('adddoc/', views.add_doc,name="adddoc"),
    path('viewp/', views.viewp,name="viewp"),
    path('addpnt/', views.addpnt,name="addpnt"),
    path('docdel(?p<int:pid>)', views.docdel,name="docdel"),
    path('addapp/', views.addappoint,name="addapp"),
    path('viewapp/', views.viewappoint,name="viewapp"),
    path('editdoc/<int:id>', views.editdoc,name="editdoc"),
    path('delp/<int:id>', views.delp,name="delp"),
    path('uptp/<int:id>', views.uptp,name="uptp"),
    path('delapp/<int:id>', views.delapp,name="delapp"),

]
