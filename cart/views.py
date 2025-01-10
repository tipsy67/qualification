from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from config.settings import LOGIN_URL
from optics.models import Product
from .cart import Cart


def cart_add(request, product_id):
    if request.user.is_authenticated:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=1, )
        url = request.META.get('HTTP_REFERER') + "#product_" +str(product_id)
        return redirect(url)
    else:
        url = reverse(LOGIN_URL)+'?next='+request.META.get('HTTP_REFERER')+ "#product_" +str(product_id)
        return redirect(url)

