from django import forms
from goods.models import Goods, Categories, Address


class AdForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), empty_label='Категория не выбрана',
                                      label='Категория', required=True,
                                      widget=forms.Select(attrs={'class': "categories__input"}))
    address = forms.ModelChoiceField(queryset=Address.objects.all(), empty_label='Адрес не выбран',
                                      label='Местоположение', required=True,
                                      widget=forms.Select(attrs={'class': "categories__input"}))

    class Meta:
        model = Goods
        fields = ['name','image', 'category', 'address', 'condition', 'description', 'price']

        labels = {
            'name': 'Название товара',
            'image': 'Фотографии',
            'category': 'Категория',
            'description': 'Описание',
            'price': 'Цена',
        }

        # cостояние бу/новое

        widgets = {
            'condition': forms.CheckboxInput,
            'name': forms.TextInput(attrs={'placeholder': 'Введите название', 'class': "add-product__name-input"}),
            'image': forms.FileInput(attrs={'class': "photo-upload__input", 'hidden': True, 'id': "fileInput"}),
            'description': forms.Textarea(attrs={'placeholder': 'Опишите ваш товар или услугу', 'class': "decription-area"}),
            'price': forms.NumberInput(attrs={'placeholder': 'Введите цену', 'class': "price__input"}),
        }

class GoodsFilterForm(forms.Form):
    query = forms.CharField(
        label='Поиск по названию',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Введите название'})
    )
    category = forms.ModelChoiceField(
        queryset=Categories.objects.all(),
        label='Категория',
        required=False,
        empty_label='Все категории',
        widget=forms.Select(attrs={'class': "categories__input"})
    )
    min_price = forms.IntegerField(
        label='Минимальная цена',
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'От', 'class' :"price__input"})
    )
    max_price = forms.IntegerField(
        label='Максимальная цена',
        required=False,
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'До', 'class' :"price__input"})
    )
    address = forms.ModelChoiceField(
        queryset=Address.objects.all(),
        label='Местоположение',
        required=False,
        empty_label='Не указано',
        widget=forms.Select(attrs={'class': "categories__input"})
    )

