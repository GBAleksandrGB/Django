from .views import user_create, users, user_update, user_delete, category_create, categories, category_update, \
    category_delete, product_create, products, product_read, product_update, product_delete, UsersListView, \
    ProductCategoryCreateView, ProductCategoryUpdateView, ProductCategoryDeleteView, ProductDetailView, UserCreateView, \
    UserUpdateView, UserDeleteView
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/read/', UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),

    path('categories/create/', ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', categories, name='categories'),
    path('categories/update/<int:pk>/', ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/category/<int:pk>/', product_create, name='product_create'),
    path('products/read/category/<int:pk>/', products, name='products'),
    path('products/read/<int:pk>/', ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', product_update, name='product_update'),
    path('products/delete/<int:pk>/', product_delete, name='product_delete'),
]
