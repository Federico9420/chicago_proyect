from django.shortcuts import render, redirect, get_object_or_404 
from .models import Cart, CartItem
from Chicago.models import Producto, Talle, Stock
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def index_store(request):
    return render(request, 'Store/index_store.html')

def category_view(request, category_name):
    productos = Producto.objects.prefetch_related('stocks__talle').filter(categoria=category_name)
    context = {
        'productos': productos,
        'category_name': category_name
    }
    return render(request, 'Store/category.html', context)

@login_required
def cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
   
    items_with_subtotals = []
    total = 0

    for item in items:
        subtotal = item.product.precio * item.quantity
        items_with_subtotals.append({
            'descripcion': item.product.descripcion,
            'precio': item.product.precio,
            'cantidad': item.quantity,
            'subtotal': subtotal
        })
        total += subtotal

    context = {
        'items': items_with_subtotals,
        'total': total,
    }
    return render(request, 'Store/cart.html', context)

@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        talle_id = request.POST.get('talle_id')
        talle = get_object_or_404(Talle, id=talle_id)
        producto = get_object_or_404(Producto, id=product_id)

        stock = Stock.objects.filter(producto=producto, talle=talle).first()
        if not stock or stock.cantidad <= 0:
            messages.error(request, "Ese talle no está disponible.")
            return redirect('Store:category_view', category_name=producto.categoria.nombre)

        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=producto,
            talle=talle
        )

        if not created:
            cart_item.quantity += 1
        cart_item.save()

        messages.success(request, f"{producto.descripcion} (Talle {talle.nombre}) agregado al carrito.")
        return redirect('Store:cart')

    return redirect('Store:index_store')
