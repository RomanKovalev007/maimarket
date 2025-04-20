from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from goods.models import Goods


class MainPage(ListView):
    template_name = 'main/index.html'
    context_object_name = 'ads'
    title_page = 'Главная страница'
    cat_selected = 0

    def get_queryset(self):
        return Goods.objects.filter(is_published=1).select_related('category')

def index(request):
    data = {'title': 'MAI_market'}
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')