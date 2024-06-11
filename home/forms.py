from django import forms

from home.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'address': 'Адрес',
            'phone': 'Телефон',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Введите вашу фамилию'}),
            'address': forms.TextInput(attrs={'placeholder': 'Введите ваш адрес'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Введите ваш телефон'}),
        }

