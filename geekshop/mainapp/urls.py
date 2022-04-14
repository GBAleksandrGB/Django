from django.urls import path
from .views import main, products, contact


urlpatterns = [
    path('', main, name='main'),
    path('products/', products, name='products'),
    path('contact/', contact, name='contact'),
    path('products_all/', products, name='products_all'),
    path('products_home/', products, name='products_home'),
    path('products_office/', products, name='products_office'),
    path('products_modern/', products, name='products_modern'),
    path('products_classic/', products, name='products_classic'),
]
