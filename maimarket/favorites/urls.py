from django.urls import path, reverse_lazy
from . import views

app_name = 'favorites'


urlpatterns = [
    path('fav_list/', views.fav_list, name='fav_list'),
    path('api/change/<int:ad_id>/', views.fav_change, name='change'),
]