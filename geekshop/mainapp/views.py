from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, ProductCategory
from basketapp.models import Basket
from random import sample


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


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def products(request, pk=None):
    title = 'Каталог'
    links_menu = [
        {'href': 'main', 'name': 'Домой'},
        {'href': 'products', 'name': 'Продукты'},
        {'href': 'contact', 'name': 'Контакты'},
    ]
    links_products = ProductCategory.objects.all()

    basket = get_basket(request.user)
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': "Все"}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'links_products': links_products,
            'category': category,
            'products': products,
            'basket': basket,
        }
        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'links_products': links_products,
        'same_products': same_products,
        'hot_product': hot_product,
        'basket': basket,
    }
    return render(request, 'mainapp/products.html', content)


def product(request, pk):
    title = 'Продукты'
    links_menu = [
        {'href': 'main', 'name': 'Домой'},
        {'href': 'products', 'name': 'Продукты'},
        {'href': 'contact', 'name': 'Контакты'},
    ]

    content = {
        'title': title,
        'links_menu': links_menu,
        'links_products': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)


def contact(request):
    title = 'Контакты'
    links_menu = [
        {'href': 'main', 'name': 'Домой'},
        {'href': 'products', 'name': 'Продукты'},
        {'href': 'contact', 'name': 'Контакты'},
    ]
    content = {'title': title, 'links_menu': links_menu}
    return render(request, 'mainapp/contact.html', content)
