"""
URL configuration for htmlproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('institute/',institute,name='institute'),
    path('animation/',animation,name='animation'),
    path('application/',application,name='application'),
    path('form/',form,name='form'),
    path('transform/',transform,name='transform'),
    path('jspiderinfo/',jspiderinfo,name='jspiderinfo'),
    path('table/',table,name='table'),
    path('bootstrap/',bootstrap,name='bootstrap'),
    path('bscart/',bscart,name='bscart'),
    path('divtags/',divtags,name='divtags'),
    path('cart/',cart,name='cart'),
    path('horizontalcards/',horizontalcards,name='horizontalcards'),
    path('form1/',form1,name='form1'),
    path('timetable/',timetable,name='timetable'),
    path('table2/',table2,name='table2'),

]
