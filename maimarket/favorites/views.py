from audioop import reverse
from itertools import product

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView

from favorites.models import Favorites
from goods.models import Goods


@login_required
def fav_list(request):
    ads = Favorites.objects.filter(user=request.user)
    data = {'ads': ads}
    return render(request, 'favorites/fav_list.html', data)

@login_required
def fav_add(request, ad_slug):
    product = Goods.objects.get(slug=ad_slug)
    favs = Favorites.objects.filter(user=request.user, product=product)
    if not favs.exists():
        Favorites.objects.create(user=request.user, product=product)
    return redirect(request.META['HTTP_REFERER'])



def fav_change(request, ad_slug):
    ...

def fav_delete(request, ad_slug):
    product = Goods.objects.get(slug=ad_slug)
    favs = Favorites.objects.filter(user=request.user, product=product)
    if favs.exists():
        favs.delete()
    return redirect(request.META['HTTP_REFERER'])