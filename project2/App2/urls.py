from django.urls import path
from App2 import views


urlpatterns=[
    path('', views.index,name='index'),
    
]