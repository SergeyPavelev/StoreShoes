from django.shortcuts import render, HttpResponsePermanentRedirect
from products.models import ProductCategory, Products, Basket
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def index(request):
    context = {
        'title': 'Store'
    }

    return render(request, 'products/index.html', context)


def products(request, category_id=None, page_number=1):
    products = Products.objects.filter(category_id=category_id) if category_id else Products.objects.all()
    
    per_page = 3
    paginator = Paginator(products, per_page=per_page)
    products_paginator = paginator.page(page_number)
    
    context = {
        'title': 'Store-products',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
    }

    return render(request, 'products/products.html', context)

@login_required
def basket_add(request, product_id):
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    
    return HttpResponsePermanentRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponsePermanentRedirect(request.META['HTTP_REFERER'])
