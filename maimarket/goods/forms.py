from django import forms

from goods.models import Goods, Categories


class AdForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Categories.objects.all(), empty_label='Категория не выбрана',
                                      label='Категория', required=True,
                                      widget=forms.Select(attrs={'class': "categories__input"}))

    class Meta:
        model = Goods
        fields = ['name','image', 'category', 'condition', 'description', 'price']

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

