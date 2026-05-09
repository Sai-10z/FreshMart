# FILE: config/urls.py

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from store.views import welcome

# ACCOUNTS
from accounts.views import (
    signup,
    custom_login,
    custom_logout,
    change_password,   # ✅ ADDED
)

# STORE
from store.views import (
    home,
    customer_dashboard,
    fruits,
    vegetables,
    add_to_cart,
    cart_view,
    increase_cart,
    decrease_cart,
    remove_cart,
    update_cart_weight,
    checkout,
    razorpay_payment,
    razorpay_success,
    profile_page,
    about,
    vendor_dashboard,
    vendor_customers,
    add_product,
    edit_product,
    delete_product,
    vendor_revenue,
    vendor_inventory,
    toggle_product_status,
)

# ORDERS
from orders.views import (
    order_history,
    cancel_order,
    download_invoice,
    success,
    payment_success,
    vendor_orders,
    update_order_status,
    vendor_download_order_pdf,
    vendor_orders_export,
)

urlpatterns = [

    # ADMIN
    path('admin/', admin.site.urls),

    # HOME
    path('', welcome, name='welcome'),   # FIRST PAGE
    path('home/', home, name='home'),    # landing page

    # AUTH
    path('signup/', signup, name='signup'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),

    # CUSTOMER
    path('customer-dashboard/', customer_dashboard, name='customer_dashboard'),
    path('fruits/', fruits, name='fruits'),
    path('vegetables/', vegetables, name='vegetables'),

    # CART
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart'),
    path('cart/increase/<int:product_id>/', increase_cart, name='increase_cart'),
    path('cart/decrease/<int:product_id>/', decrease_cart, name='decrease_cart'),
    path('cart/remove/<int:product_id>/', remove_cart, name='remove_cart'),
    path('cart/update-weight/<int:product_id>/', update_cart_weight, name='update_cart_weight'),

    # CHECKOUT
    path('checkout/', checkout, name='checkout'),
    path('razorpay-payment/', razorpay_payment, name='razorpay_payment'),
    path('razorpay-success/', razorpay_success, name='razorpay_success'),
    path('payment-success/', payment_success, name='payment_success'),

    # PROFILE
    path('profile/', profile_page, name='profile_page'),
    path('change-password/', change_password, name='change_password'),  # ✅ NEW
    path('about/', about, name='about'),

    # VENDOR
    path('vendor-dashboard/', vendor_dashboard, name='vendor_dashboard'),
    path('vendor-customers/', vendor_customers, name='vendor_customers'),
    path('vendor-orders/', vendor_orders, name='vendor_orders'),
    path('vendor-revenue/', vendor_revenue, name='vendor_revenue'),
    path('vendor-inventory/', vendor_inventory, name='vendor_inventory'),

    path('add-product/', add_product, name='add_product'),
    path('edit-product/<int:product_id>/', edit_product, name='edit_product'),
    path('delete-product/<int:product_id>/', delete_product, name='delete_product'),

    # PRODUCT TOGGLE (FIXED - ONLY ONCE)
    path(
        'toggle-product/<int:product_id>/',
        toggle_product_status,
        name='toggle_product_status'
    ),

    # ORDERS
    path('orders/', order_history, name='orders'),
    path('cancel-order/<int:order_id>/', cancel_order, name='cancel_order'),
    path('download-invoice/<int:order_id>/', download_invoice, name='download_invoice'),
    path('success/', success, name='success'),

    path(
        'update-order-status/<int:order_id>/<str:status>/',
        update_order_status,
        name='update_order_status'
    ),

    path(
        'vendor-download-order/<int:order_id>/',
        vendor_download_order_pdf,
        name='vendor_download_order'
    ),

    path(
        'vendor-orders-export/',
        vendor_orders_export,
        name='vendor_orders_export'
    ),

    path('home/', home, name='home')
    
]

# MEDIA FILES (IMPORTANT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)