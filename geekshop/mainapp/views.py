from django.shortcuts import render

links_menu = [
    {'href': 'main', 'name': 'Домой'},
    {'href': 'products', 'name': 'Продукты'},
    {'href': 'contact', 'name': 'Контакты'},
]

content_links_menu = {
    'links_menu': links_menu,
}

links_products = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'products_home', 'name': 'дом'},
    {'href': 'products_office', 'name': 'офис'},
    {'href': 'products_modern', 'name': 'модерн'},
    {'href': 'products_classic', 'name': 'классика'},
]

content_links_products = {
    'links_products': links_products,
    'links_menu': links_menu,
}


def main(request):
    return render(request, 'mainapp/index.html', context=content_links_menu)


def products(request):
    return render(request, 'mainapp/products.html', context=content_links_products)


def contact(request):
    return render(request, 'mainapp/contact.html', context=content_links_menu)
