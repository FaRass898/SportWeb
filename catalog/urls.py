# catalog/urls.py
from django.urls import path
from .views import catalog, product_detail, add_review, add_to_cart, cart_detail, create_order, order_list, order_edit, order_delete

urlpatterns = [
    path('', catalog, name='catalog'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('<int:pk>/add_review/', add_review, name='add_review'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('create_order/', create_order, name='create_order'),
    path('orders/', order_list, name='order_list'),
    path('orders/<int:order_id>/edit/', order_edit, name='order_edit'),
    path('orders/<int:order_id>/delete/', order_delete, name='order_delete'),
]
