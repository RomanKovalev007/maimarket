from django.urls import path, reverse_lazy
from . import views

app_name = 'favorites'


urlpatterns = [
    path('fav_list/', views.fav_list, name='fav_list'),
    path('add/<slug:ad_slug>/', views.fav_add, name='add'),
    path('change/<slug:ad_slug>/', views.fav_change, name='change'),
    path('remove/<slug:ad_slug>/', views.fav_delete, name='remove')
]