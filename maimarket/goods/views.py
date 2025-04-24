from gc import get_objects
from itertools import product

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from favorites.models import Favorites
from goods.forms import AddAdForm
from goods.models import Goods


class AddAd(LoginRequiredMixin, CreateView):
    form_class =  AddAdForm
    template_name = 'goods/add_ad.html'
    extra_context = {'title': 'Новое объявление'}
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        w = form.save(commit=False)
        w.seller = self.request.user
        return super().form_valid(form)

def goods_list(request):
    ads = Goods.objects.filter(is_published=1)
    for ad in ads:
        if Favorites.objects.filter(user=request.user, product=ad).exists():
            ad.icon_class = "icon-red-heart"
        else:
            ad.icon_class = "icon--heart"
    data = {'ads': ads}
    return render(request, 'goods/goods_list.html', data)


def show_ad(request, ad_slug):
    ad = get_object_or_404(Goods, slug=ad_slug)
    return render(request, 'goods/ad.html', {'ad': ad})