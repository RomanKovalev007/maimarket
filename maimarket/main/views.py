from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from favorites.models import Favorites
from goods.models import Goods


def main_page(request):
    ads = Goods.objects.filter(is_published=1)
    if request.user.is_authenticated:
        for ad in ads:
            if Favorites.objects.filter(user=request.user, product=ad).exists():
                ad.is_favorite = 'is-active'
            else:
                ad.is_favorite = ''
    else:
        for ad in ads:
            ad.icon_class = "icon--heart"
    data = {'ads': ads, 'title': 'MAI Market'}
    return render(request, 'main/index.html', data)

def index(request):
    data = {'title': 'MAI_market'}
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')