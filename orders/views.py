from django.shortcuts import render, redirect
from orders.models import Order, OrderItem, OrderStatus
from menu.models import Food
from accounts.models import CustomUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def add_to_cart(request, food_id):
    customer = request.user
    food = Food.objects.get(id=food_id)

    order = Order.objects.filter(customer=customer, order_status=OrderStatus.PENDING).first()
    if not order:
        order = Order.objects.create(customer=customer)

    order_item = OrderItem.objects.filter(order=order, food=food).first()
    
    if order_item:
        order_item.quantity += 1
        order_item.save()
    else:
        OrderItem.objects.create(order=order, food=food, quantity=1)
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def cart(request):
    order = Order.objects.filter(customer=request.user, order_status=OrderStatus.PENDING).first()
    items = []
    if order:
        items = order.orderitem_set.all()

    total_price = 0
    for item in items:
        total_price += item.food.price * item.quantity
    context = {'order': order, 'items': items, 'total_price': total_price}
    return render(request, 'orders/cart.html', context=context)

@login_required
def decrease_item(request, food_id):
    food = Food.objects.get(id=food_id)
    order = Order.objects.filter(customer=request.user, order_status=OrderStatus.PENDING).first()
    order_item = OrderItem.objects.filter(order=order, food=food).first()
    if order_item.quantity > 1:
        order_item.quantity -= 1
        order_item.save()
    else:
        order_item.delete()
    return redirect("cart")

@login_required
def increase_item(request, food_id):
    food = Food.objects.get(id=food_id)
    order = Order.objects.filter(customer=request.user, order_status=OrderStatus.PENDING).first()
    order_item = OrderItem.objects.filter(order=order, food=food).first()

    order_item.quantity += 1
    order_item.save()
    return redirect("cart")

@login_required
def checkout(request):
    customer = request.user

    order = Order.objects.filter(
        customer=customer,
        order_status=OrderStatus.PENDING
    ).first()

    if not order:
        messages.error(request, "سبد خرید خالی است")
        return redirect('cart')

    if order.order_status != OrderStatus.PENDING:
        messages.error(request, "این سفارش قبلاً ثبت شده")
        return redirect('cart')

    total_price = sum(
        item.food.price * item.quantity
        for item in order.orderitem_set.all()
    )

    if customer.points >= total_price:
        customer.points -= total_price
        customer.save()

        order.order_status = OrderStatus.DELIVERING
        order.save()

        messages.success(request, "پرداخت با موفقیت انجام شد")

    else:
        messages.error(request, "موجودی کافی نمیباشد")

    print("checkout")
    return redirect('cart')
