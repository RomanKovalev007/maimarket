from django.urls import path

from main import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='home'),
    path('about/', views.about, name='about')
]
