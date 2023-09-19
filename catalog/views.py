from django.shortcuts import render

from catalog.apps import CatalogConfig
from catalog.models import Category, Product

app_name = CatalogConfig


def home_page(request):
    context = {
        'products': Product.objects.all(),
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context=context)


def contacts(request):
    if request.POST.get('name'):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"имя: {name} телефон: ({phone}) сообщение: {message}")
    context = {'title': 'Контакты'}
    return render(request, 'catalog/contacts.html', context)


def category(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории',
    }
    return render(request, 'catalog/category.html', context)


def product(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(id=pk),
        'title': f'Продукт категории {category_item.name}',
    }
    return render(request, 'catalog/product.html', context)
