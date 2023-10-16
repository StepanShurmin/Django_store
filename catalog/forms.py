from django import forms

from catalog.models import Product, Version

forbidden_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар',)


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
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    """Форма для модели Product."""

    class Meta:
        """Метаданные о модели."""
        model = Product
        exclude = ('users',)

    def clean_name(self):
        """
        Валидация поля name.
        Проверяет, что значение поля name не содержит запрещенные слова.
        Если содержит, генерирует ValidationError с сообщением об ошибке.
        """
        cleaned_data = self.cleaned_data['name']
        if cleaned_data.lower() in forbidden_words:
            raise forms.ValidationError(f'Нельзя использовать запрещённые слова {forbidden_words}!')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    """Форма для модели Version."""

    class Meta:
        """Метаданные о модели."""
        model = Version
        fields = '__all__'
