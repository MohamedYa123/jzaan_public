from django.urls import path,include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('',homepage,name="home"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns=urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)