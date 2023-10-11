from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class StyleFormMixin:
    """
    Миксин для добавления стилей к формам.
    При инициализации формы, добавляет класс 'form-control' к виджетам всех полей.
    """

    def __init__(self, *args, **kwargs):
        """
        Инициализация формы.
        Переопределяет метод __init__ для добавления класса 'form-control' к виджетам всех полей.
        """
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "available":
                field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """Форма регистрации пользователя."""
    class Meta:
        """Метаданные о модели."""
        model = User
        fields = ('email', 'password1', 'password2',)


class UserForm(StyleFormMixin, UserChangeForm):
    """Форма редактирования пользователя."""
    class Meta:
        """Метаданные о модели."""
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'country', 'avatar',)

    def __init__(self, *args, **kwargs):
        """
        Инициализация формы.
        Переопределяет метод __init__ для скрытия поля password.
        """
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
