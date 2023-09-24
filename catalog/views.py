from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.apps import CatalogConfig
from catalog.models import Category, Product

app_name = CatalogConfig


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/product.html'
    extra_context = {'title': 'Главная'}


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"имя: {name} телефон: ({phone}) сообщение: {message}")
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category.html'
    extra_context = {'title': 'Категории'}


class ProductListView(ListView):
    template_name = 'catalog/product.html'
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Продукт категории {category_item.name}'

        return context_data
