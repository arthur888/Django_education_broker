"""SiteEdu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.template.context_processors import static

from SiteEdu import settings
from  nexusite import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.index),
    url(r'^checkuser/$', views.checkuser),


    url(r'^createstudent_1/$', views.createstudent_1),
    url(r'^createstudent_2/$', views.createstudent_2),
    url(r'^createstudent_3/$', views.createstudent_3),
    url(r'^createstudent_4/$', views.createstudent_4),

    url(r'^createteacher_1/$', views.createteacher_1),
    url(r'^createteacher_2/$', views.createteacher_2),
    url(r'^createteacher_3/$', views.createteacher_3),
    url(r'^createteacher_4/$', views.createteacher_4),

    url(r'^userinfo/$', views.view_userprofile),
    url(r'^teacherinfo/$', views.view_teacherprofile),
    url(r'^backgroundcheck/$', views.view_backgroundcheck),
    url(r'^contact/$', views.view_contact),
    url(r'^blog/$', views.view_blogs),
    url(r'^blog/create/$', views.crete_blog),
    url(r'^blog/my/$', views.view_myblogs),
    url(r'^blog/detail/(?P<blog_id>\d+)/$', views.view_blog_detail),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^postrequestst/$', views.post_request_s),
    url(r'^postrequestst/viewrespond/$', views.view_respondst),
    url(r'^academirecord/$', views.crete_academirecord),
    url(r'^clientsrecommendation/$', views.view_clientsrecommendation),
    url(r'^detailprofilet/(?P<tid>\d+)/$', views.view_profilet_detail),
    url(r'^booking/(?P<tid>\d+)/$', views.view_booking),
]
