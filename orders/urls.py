from django.urls import path
from . import views

urlpatterns = [

    path(
        'orders/',
        views.order_history,
        name='orders'
    ),

    path(
        'cancel-order/<int:order_id>/',
        views.cancel_order,
        name='cancel_order'
    ),

    path(
        'download-invoice/<int:order_id>/',
        views.download_invoice,
        name='download_invoice'
    ),

    path(
        'success/',
        views.success,
        name='success'
    ),

    path(
        'vendor-orders/',
        views.vendor_orders,
        name='vendor_orders'
    ),

    path(
        'update-order-status/<int:order_id>/<str:status>/',
        views.update_order_status,
        name='update_order_status'
    ),

    path(
        'payment-success/',
        views.payment_success,
        name='payment_success'
    ),

    path(
        'vendor-download-order/<int:order_id>/',
        views.vendor_download_order_pdf
    ),

    path(
        'vendor-orders-export/',
        views.vendor_orders_export,
        name='vendor_orders_export'
    ),

]