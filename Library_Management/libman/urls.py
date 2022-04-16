from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^book/$', views.view_books, name='view_books'),
    url(r'^employer/$', views.view_employer, name='view_employer'),
    url(r'^issue/$', views.view_issue, name='view_issue'),
    url(r'^contact/$', views.contact, name='contact'),
]
