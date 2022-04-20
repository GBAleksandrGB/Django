from django.shortcuts import render

from .models import Product


def main(request):
    title = 'Главная'
    links_menu = [
        {'href': 'main', 'name': 'Домой'},
        {'href': 'products', 'name': 'Продукты'},
        {'href': 'contact', 'name': 'Контакты'},
    ]
    products = Product.objects.all()[:4]
    content = {
        'title': title,
        'products': products,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = 'Каталог'
    links_menu = [
        {'href': 'main', 'name': 'Домой'},
        {'href': 'products', 'name': 'Продукты'},
        {'href': 'contact', 'name': 'Контакты'},
    ]
    links_products = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]
    content = {'title': title, 'links_menu': links_menu, 'links_products': links_products}
    print(pk)
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'Контакты'
    links_menu = [
        {'href': 'main', 'name': 'Домой'},
        {'href': 'products', 'name': 'Продукты'},
        {'href': 'contact', 'name': 'Контакты'},
    ]
    content = {'title': title, 'links_menu': links_menu}
    return render(request, 'mainapp/contact.html', content)
