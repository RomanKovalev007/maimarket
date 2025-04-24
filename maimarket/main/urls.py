from django.urls import path

from main import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('about/', views.about, name='about')
]
