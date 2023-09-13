from django.shortcuts import render


def home_page(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.POST.get('name'):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"имя: {name} телефон: ({phone}) сообщение: {message}")
    return render(request, 'catalog/contacts.html')