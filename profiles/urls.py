""" Profile URLs """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('order_history/<order_number>',
         views.order_history, name='order_history'),
    path("wishlist/add_to_wishlist", views.add_to_whishlist, name="user_wishlist"),
]
