from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label=_('Email адрес')
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': _('Имя пользователя'),
            'password1': _('Пароль'),
            'password2': _('Подтверждение пароля'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})