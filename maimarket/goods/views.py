from gc import get_objects

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

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

class GoodsList(ListView):
    template_name = 'goods/goods_list.html'
    context_object_name = 'ads'
    title_page = 'Список товаров'
    cat_selected = 0

    def get_queryset(self):
        return Goods.objects.filter(is_published=1).select_related('category')


def show_ad(request, ad_slug):
    ad = get_object_or_404(Goods, slug=ad_slug)
    return render(request, 'goods/ad.html', {'ad': ad})