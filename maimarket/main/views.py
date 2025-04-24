from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from favorites.models import Favorites
from goods.models import Goods


def main_page(request):
    ads = Goods.objects.filter(is_published=1)
    for ad in ads:
        if Favorites.objects.filter(user=request.user, product=ad).exists():
            ad.icon_class = "icon-red-heart"
        else:
            ad.icon_class = "icon--heart"
    data = {'ads': ads}
    return render(request, 'main/index.html', data)

def index(request):
    data = {'title': 'MAI_market'}
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')