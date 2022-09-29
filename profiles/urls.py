""" Profile URLs """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile/orders', views.user_order_history, name='user_order_history'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("wishlist/", views.view_wishlist, name="wishlist"),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path("wishlist/add_to_wishlist/<int:item_id>", views.add_to_whishlist, name="add_to_wishlist"),
]
