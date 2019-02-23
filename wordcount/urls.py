
from django.urls import  path
from . import views

urlpatterns = [
    path('', views.homepage,name='home'),
    path('counts', views.counts,name="counts"),
    path('about', views.about,name='about')
]
