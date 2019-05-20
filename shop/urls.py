"""Ecommerce_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from.import views

urlpatterns = [
     path('', views.index, name = "ShopHome"),
     path('about/', views.about, name="AboutUs"),
     path('contact/', views.contact, name="ContactUs"),
     path('tracker/', views.tracker, name="TrackerStatus"),
     path('search/', views.search, name="Search"),
     path('productView/', views.productView, name="ProductView"),
     path('checkout/', views.checkout, name="Checkout"),

]