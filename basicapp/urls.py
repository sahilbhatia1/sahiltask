from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
	 path('register/', views.registerhtml,name='register'),
	 path('signup/', views.save_user,name='signup'),
	 path('verifymobile/', views.verifymobile,name='verifymobile'),


]

