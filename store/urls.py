# FILE: store/urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'customer-dashboard/',
        views.customer_dashboard,
        name='customer_dashboard'
    ),

    path(
        'fruits/',
        views.fruits,
        name='fruits'
    ),

    path(
        'vegetables/',
        views.vegetables,
        name='vegetables'
    ),

    path(
        'add-to-cart/<int:product_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        views.cart_view,
        name='cart'
    ),

    path(
        'cart/increase/<int:product_id>/',
        views.increase_cart,
        name='increase_cart'
    ),

    path(
        'cart/decrease/<int:product_id>/',
        views.decrease_cart,
        name='decrease_cart'
    ),

    path(
        'cart/remove/<int:product_id>/',
        views.remove_cart,
        name='remove_cart'
    ),

    path(
        'cart/update-weight/<int:product_id>/',
        views.update_cart_weight,
        name='update_cart_weight'
    ),

    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    # Razorpay flow
    path(
        'razorpay-payment/',
        views.razorpay_payment,
        name='razorpay_payment'
    ),

    path(
        'razorpay-success/',
        views.razorpay_success,
        name='razorpay_success'
    ),

    path(
        'payment-success/',
        views.payment_success,
        name='payment_success'
    ),

    # Profile page
    path(
        'profile/',
        views.profile_page,
        name='profile_page'
    ),

    path(
        'about/',
        views.about,
        name='about'
    ),

    # Vendor panel
    path(
        'vendor-dashboard/',
        views.vendor_dashboard,
        name='vendor_dashboard'
    ),

    path(
        'vendor-customers/',
        views.vendor_customers,
        name='vendor_customers'
    ),

    # Product CRUD only
    path(
        'add-product/',
        views.add_product,
        name='add_product'
    ),

    path(
        'edit-product/<int:product_id>/',
        views.edit_product,
        name='edit_product'
    ),

    path(
        'delete-product/<int:product_id>/',
        views.delete_product,
        name='delete_product'
    ),
]