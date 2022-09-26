""" Profiles views """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def dashboard(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profiles/dashboard.html'
    context = {
        "on_profile_page": True
    }

    return render(request, template, context)


@login_required
def profile(request):
    """ Display the user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Order history """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from-profile': True,
    }

    return render(request, template, context)


@login_required
def wishlist(request):
    products = Product.objects.filter(user_wishlist=request.user)

    context = {
        'products': products,
    }
    return render(request, "profiles/wishlist.html", context)

@login_required
def add_to_whishlist(request, item_id):
    """ Wishlist """
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    if product.user_wishlist.filter(id=request.user.id).exists():
        product.user_wishlist.remove(request.user)
        messages.success(request, f'{product.name} has been removed from your Whislist')
    else:
        product.user_wishlist.add(request.user)
        messages.success(request, f'{product.name} has been added to your Whislist')

    return redirect(redirect_url)
