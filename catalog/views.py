from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.apps import CatalogConfig
from catalog.models import Category, Product

app_name = CatalogConfig


class HomeListView(ListView):
    """Выводит на экран главную страницу с товарами."""
    model = Product
    template_name = 'catalog/product.html'
    extra_context = {'title': 'Главная'}


class ContactsView(TemplateView):
    """Выводит на экран страницу с контактными данными."""
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        """Выводит в консоль данные из формы обратной связи."""
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"имя: {name} телефон: ({phone}) сообщение: {message}")
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """
        Возвращает словарь с контекстными данными,
        для отображения заголовка станицы.
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context


class CategoryListView(ListView):
    """Выводит на экран страницу с категориями товаров."""
    model = Category
    template_name = 'catalog/category.html'
    extra_context = {'title': 'Категории'}


class ProductListView(ListView):
    template_name = 'catalog/product.html'
    model = Product

    def get_queryset(self):
        """
        Фильтрует набор запросов и возвращает только
        объект с соответствующим идентификатором.
        """
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        """
        Возвращает словарь с контекстными данными,
        для отображения заголовка станицы.
        """
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Продукт категории {category_item.name}'

        return context_data
