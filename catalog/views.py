# from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, DetailView

from catalog.apps import CatalogConfig
from catalog.forms import ProductForm, VersionForm
from catalog.models import Category, Product, Version

app_name = CatalogConfig


class HomeListView(ListView):
    """Выводит на экран главную страницу с товарами."""
    model = Product
    template_name = 'catalog/product_list.html'
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
    """Выводит на экран страницу с товарами."""
    template_name = 'catalog/product_list.html'
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


class ProductCreateView(CreateView):
    """Создает новый продукт."""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    """Обновляет продукт."""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_view')

    def get_success_url(self):
        """Возвращает URL для перенаправления после успешного сохранения формы."""
        return reverse('catalog:product_edit', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        """Возвращает контекст данных для отображения формы."""
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        """Обрабатывает действия при валидной форме."""
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    """Выводит информацию о продукте."""
    model = Product


class ProductDeleteView(DeleteView):
    """Удаляет продукт."""
    model = Product
    success_url = reverse_lazy('catalog:home')
