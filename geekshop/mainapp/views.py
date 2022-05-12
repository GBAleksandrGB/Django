from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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


def get_hot_product():
    products = Product.objects.all()
    return sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def products(request, pk=None, page=1):
    title = 'Продукты'
    links_menu = [
        {'href': 'main', 'name': 'Домой'},
        {'href': 'products', 'name': 'Продукты'},
        {'href': 'contact', 'name': 'Контакты'},
    ]
    links_products = ProductCategory.objects.filter(is_active=True)

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'Все'
            }
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        paginator = Paginator(products, 2)

        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'links_products': links_products,
            'category': category,
            'products': products_paginator,
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
