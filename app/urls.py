from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('func/b32encode', views.encode, name='encode'),
    path('func/b32decode', views.decode, name='decode'),
    path('func/otp', views.getotp, name='otp'),
    path('func/url', views.geturl, name='url'),
    path('func/verify', views.verify, name='verify')
]
