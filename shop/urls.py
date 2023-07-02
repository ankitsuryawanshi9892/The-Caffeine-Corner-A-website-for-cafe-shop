from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name= "Home"),
    path("about/", views.about, name= "about"),
    path("menu/", views.menu, name= "menu"),
    path("testimonial/", views.testimonial, name= "testimonial"),
    path('shop/testimonial/', views.testimonial, name='testimonial'),
]

