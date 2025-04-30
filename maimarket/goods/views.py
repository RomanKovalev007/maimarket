from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from favorites.models import Favorites
from goods.forms import AdForm
from goods.models import Goods


class AddAd(LoginRequiredMixin, CreateView):
    form_class =  AdForm
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
    context = {
        'ads': ads,
        'title': 'Лента объявлений'
    }
    return render(request, 'goods/goods_list.html', context)


def show_ad(request, ad_slug):
    ad = get_object_or_404(Goods, slug=ad_slug)
    context = {
        'ad': ad,
        'title': ad.name
    }
    return render(request, 'goods/product-card.html', context)


def edit_ad(request, ad_slug):
    ad = get_object_or_404(Goods, slug=ad_slug)

    if request.user != ad.seller:
        raise PermissionDenied("У вас нет прав для редактирования этого объявления")

    if request.method == 'POST':
        form = AdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            updated_ad = form.save()
            return redirect('goods:ad', ad_slug=updated_ad.slug)
    else:
        form = AdForm(instance=ad)

    context = {
        'form': form,
        'ad': ad,
        'title': 'Редактирование объявления'
    }
    return render(request, 'goods/edit_ad.html', context)

def remove_ad(request, ad_slug):
    ad = Goods.objects.get(slug=ad_slug)
    if ad.is_published:
        ad.is_published = False
        ad.save()
    else:
        ad.is_published = True
        ad.save()
    return redirect(request.META['HTTP_REFERER'])

