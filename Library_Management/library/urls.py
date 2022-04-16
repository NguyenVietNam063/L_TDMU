"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from xml.dom.minidom import Document
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from libman import views as core_views
from django.views.generic import TemplateView
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView
from django.views.static import serve
from django.conf.urls.static import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.redir, name='redirect_view'),
    url('social/', include('social.apps.django_app.urls', namespace='social')),
    url('accounts/', include('allauth.urls')),
    url( 'login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^library/', include('libman.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]