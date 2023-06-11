from django.contrib import admin
from django.urls import path
from .views import Mainview
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Mainview/', Mainview.as_view(), name="Mainview"),
    path('signup/', views.signup,name='signup'),

    ]
