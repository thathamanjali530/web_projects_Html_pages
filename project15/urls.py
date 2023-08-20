"""
URL configuration for project15 project.

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
    path('student/',student,name='student.html'),
    path('seminar/',seminar,name='seminar.html'),
    path('timeTable/',timeTable,name='timeTable.html'),
    path('studentlist/',studentlist,name='studentlist.html'),
    path('flipkart/',flipkart,name='flipkart.html'),
    path('employee/',employee,name='employee.html'),
    path('colour/',colour,name='colour.html'),
    path('subject/',subject,name='subject.html'),
    path('calculation/',calculation,name='calculation.html'),
    path('vedio/',vedio,name='vedio.html'),
    path('positions/',positions,name='positions.html'),
    path('buttons/',buttons,name='buttons.html'),
    path('local/',local,name='local.html'),
    path('boxes/',boxes,name='boxes.html'),
    path('gotop/',gotop,name='gotop.html'),
    path('zomoto/',zomoto,name='zomoto.html'),
    path('Amara/',Amara,name='Amara.html'),
    
    
    
]

