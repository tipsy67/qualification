from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from config.settings import LOGIN_URL
from optics.models import Product
from .cart import Cart
from .forms import CartAddProductForm


def cart_add(request, product_id):
    if request.user.is_authenticated:
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        if request.method == 'POST':
            form = CartAddProductForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                cart.add(product=product, quantity = cd['quantity'], override_quantity = cd['override'])
        else:
            cart.add(product=product, quantity=1, )

        url = request.META.get('HTTP_REFERER') + "#product_" +str(product_id)
        return redirect(url)
    else:
        url = reverse(LOGIN_URL)+'?next='+request.META.get('HTTP_REFERER')+ "#product_" +str(product_id)
        return redirect(url)

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                            'quantity': item['quantity'],
                            'override': True})
    return render(request, 'cart/cart-list.html', {'cart': cart})

# @require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')