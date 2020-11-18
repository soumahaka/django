"""advancedtopics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from classapp import views
from django.conf.urls import url
urlpatterns = [
    path("", views.SchoolListView.as_view(), name="schoollistpage"),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name="schooldetail"),
    #c'est la maniere de linker la detailview, pk affiche les detail des
    #instances de la table en utilisant leur id
    path('admin/', admin.site.urls),
    path("create/", views.SchoolCreateView.as_view(), name="create"),
    path('update/<slug:pk>/', views.SchoolUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.SchoolDeleteView.as_view(), name="delete" ),

]
