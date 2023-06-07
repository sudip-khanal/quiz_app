from django.contrib import admin
from django.urls import path
from .views import Homeview

urlpatterns = [path("", Homeview.as_view(), name="home")]
