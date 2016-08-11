from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^about$', views.about, name='about'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^index$', views.index, name='index'),
    url(r'^projects$', views.projects, name='projects'),
    url(r'^typo$', views.typo, name='typo'),

]
