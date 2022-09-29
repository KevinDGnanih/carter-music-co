""" Profiles views """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def dashboard(request):
    """ View the profile dashboard """
    template = 'profiles/dashboard.html'

    return render(request, template)


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

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def user_order_history(request):
    """ Display the user's order history """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()

    template = 'profiles/orders_history.html'
    context = {
        'orders': orders,
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
def view_wishlist(request):
    """ A view that renders the user wishlist contente page """
    product = Product.objects.all()

    context = {
        'wishlist': product,
    }

    return render(request, "profiles/wishlist.html", context)


@login_required
def add_to_whishlist(request, item_id):
    """ Add the product to the user wishlist """
    product = get_object_or_404(Product, pk=item_id)

    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
        messages.success(request, f'{product.name} has been removed from your Whislist')
    else:
        product.users_wishlist.add(request.user)
        messages.success(request, f'{product.name} has been added to your Whislist')

    return HttpResponseRedirect(request.META["HTTP_REFERER"])
