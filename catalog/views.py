# catalog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, 'Товар успешно добавлен')
    return redirect('cart_detail')


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'catalog/cart_detail.html', {'cart_items': cart_items})


@login_required
def create_order(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    if not cart.products.exists():
        messages.error(request, 'Ваша корзина пуста.')
        return redirect('catalog')

    order = Order.objects.create(user=request.user)
    for item in CartItem.objects.filter(cart=cart):
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
    cart.products.clear()
    messages.success(request, 'Заказ успешно создан')
    return redirect('order_list')


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'catalog/order_list.html', {'orders': orders})


@login_required
def order_edit(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        # Обработка данных формы
        order.status = request.POST.get('status', order.status)
        order.save()
        messages.success(request, 'Заказ успешно обновлен')
        return redirect('order_list')
    return render(request, 'catalog/order_edit.html', {'order': order})


@login_required
def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    order.delete()
    messages.success(request, 'Заказ успешно удален')
    return redirect('order_list')
