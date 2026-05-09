from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q, Sum
from django.http import HttpResponse
from datetime import date

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from orders.models import Order

from .models import Order, OrderItem

import csv
from calendar import month_name

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

from reportlab.platypus import Image
import os
from django.conf import settings

@login_required
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    ).prefetch_related(
        'orderitem_set',
        'orderitem_set__product'
    ).order_by('-id')

    return render(request, 'order_history.html', {
        'orders': orders
    })


@login_required
def cancel_order(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    if order.order_status == 'Pending':
        order.order_status = 'Cancelled'
        order.save()

    return redirect('/orders/')


@staff_member_required
def vendor_orders(request):

    query = request.GET.get('q', '')

    all_orders = Order.objects.all().prefetch_related(
        'orderitem_set',
        'orderitem_set__product'
    )

    if query:
        all_orders = all_orders.filter(
            Q(user__username__icontains=query) |
            Q(customer_name__icontains=query) |
            Q(phone__icontains=query)
        )

    all_orders = all_orders.order_by('-id')

    active_orders = all_orders.exclude(
        order_status__in=['Delivered', 'Cancelled']
    )

    delivered_history = all_orders.filter(
        order_status='Delivered'
    )

    cancelled_orders = all_orders.filter(
        order_status='Cancelled'
    )

    total_revenue = Order.objects.aggregate(
        total=Sum('total_price')
    )['total'] or 0

    delivered_revenue = Order.objects.filter(
        order_status='Delivered'
    ).aggregate(
        total=Sum('total_price')
    )['total'] or 0

    today_revenue = Order.objects.filter(
        created_at__date=date.today()
    ).aggregate(
        total=Sum('total_price')
    )['total'] or 0

    return render(request, 'vendor_orders.html', {
        'orders': all_orders,
        'active_orders': active_orders,
        'delivered_history': delivered_history,
        'cancelled_orders': cancelled_orders,
        'total_orders': all_orders.count(),
        'pending_orders': active_orders.count(),
        'delivered_orders': delivered_history.count(),
        'total_revenue': total_revenue,
        'delivered_revenue': delivered_revenue,
        'today_revenue': today_revenue,
        'query': query
    })


@staff_member_required
def update_order_status(request, order_id, status):

    valid_status = [
        'Pending',
        'Packed',
        'Shipped',
        'Delivered'
    ]

    if status not in valid_status:
        return redirect('/vendor-orders/')

    order = get_object_or_404(
        Order,
        id=order_id
    )

    if order.order_status in ['Delivered', 'Cancelled']:
        return redirect('/vendor-orders/')

    order.order_status = status
    order.save()

    return redirect('/vendor-orders/')


@login_required
def download_invoice(request, order_id):

    order = get_object_or_404(Order, id=order_id, user=request.user)
    items = OrderItem.objects.filter(order=order)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=invoice_order_{order.id}.pdf'

    pdf = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    logo_path = os.path.join(settings.BASE_DIR, 'static/images/logo.png')

    # BORDER
    pdf.setStrokeColor(colors.lightgrey)
    pdf.rect(20, 20, width - 40, height - 40)

    # HEADER BAR
    pdf.setFillColor(colors.green)
    header_y = height - 75
    header_height = 45
    pdf.rect(20, header_y, width - 40, header_height, fill=1)

    # 🔥 FIXED LOGO POSITION
    if os.path.exists(logo_path):
        logo_width = 30
        logo_height = 30
        logo_x = width - 60
        logo_y = header_y + (header_height - logo_height) / 2

        pdf.drawImage(
            logo_path,
            logo_x,
            logo_y,
            width=logo_width,
            height=logo_height,
            preserveAspectRatio=True,
            mask='auto'
        )

    # TITLE
    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(35, height - 57, "FreshMart Invoice")

    pdf.setFillColor(colors.black)
    y = height - 105

    # DETAILS
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(35, y, "Invoice Details")

    y -= 22
    pdf.setFont("Helvetica", 10)

    pdf.drawString(35, y, f"Order ID: {order.id}")
    pdf.drawString(320, y, f"Date: {order.created_at.strftime('%d-%m-%Y')}")

    y -= 18
    pdf.drawString(35, y, f"Customer: {order.customer_name}")

    y -= 18
    pdf.drawString(35, y, f"Phone: {order.phone}")

    y -= 18
    pdf.drawString(35, y, f"Payment: {order.payment_method}")

    y -= 18
    pdf.drawString(35, y, f"Status: {order.order_status}")

    y -= 18

    clean_address = (
        order.address.replace("\n", " ")
        .replace("\r", " ")
        .replace("■", "")
        .replace("█", "")
        .strip()
    )

    pdf.drawString(35, y, f"Address: {clean_address[:75]}")

    # TABLE HEADER
    y -= 35
    pdf.setFillColor(colors.HexColor("#EAEAEA"))
    pdf.rect(30, y, width - 60, 22, fill=1)

    pdf.setFillColor(colors.black)
    pdf.setFont("Helvetica-Bold", 10)

    pdf.drawString(38, y + 7, "Product")
    pdf.drawString(240, y + 7, "Qty")
    pdf.drawString(290, y + 7, "Weight")
    pdf.drawString(380, y + 7, "Price")
    pdf.drawString(475, y + 7, "Subtotal")

    y -= 22
    pdf.setFont("Helvetica", 10)

    for item in items:
        pdf.line(30, y, width - 30, y)

        pdf.drawString(38, y - 15, item.product.name[:28])
        pdf.drawString(242, y - 15, str(item.quantity))
        pdf.drawString(292, y - 15, item.weight)
        pdf.drawString(380, y - 15, f"Rs.{item.price}")
        pdf.drawString(475, y - 15, f"Rs.{item.subtotal}")

        y -= 24

        if y < 130:
            pdf.showPage()
            y = height - 50

    pdf.line(30, y, width - 30, y)

    y -= 38
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawRightString(width - 35, y, f"Total Amount: Rs.{order.total_price}")

    y -= 45
    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawString(35, y, "Thank you for shopping with FreshMart!")

    y -= 18
    pdf.drawString(35, y, "Fresh Fruits • Fresh Vegetables • Fast Delivery")

    pdf.save()
    return response


@login_required
def success(request):
    return render(request, 'success.html')


@login_required
def payment_success(request):
    return render(request, 'payment_success.html')

@staff_member_required
def vendor_download_order_pdf(request, order_id):

    order = get_object_or_404(Order, id=order_id)
    items = OrderItem.objects.filter(order=order)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=order_{order.id}.pdf'

    pdf = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    logo_path = os.path.join(settings.BASE_DIR, 'static/images/logo.png')

    # BORDER
    pdf.setStrokeColor(colors.lightgrey)
    pdf.rect(20, 20, width - 40, height - 40)

    # HEADER BAR
    pdf.setFillColor(colors.darkgreen)
    header_y = height - 75
    header_height = 45
    pdf.rect(20, header_y, width - 40, header_height, fill=1)

    # 🔥 FIXED LOGO POSITION
    if os.path.exists(logo_path):
        logo_width = 30
        logo_height = 30
        logo_x = width - 60
        logo_y = header_y + (header_height - logo_height) / 2

        pdf.drawImage(
            logo_path,
            logo_x,
            logo_y,
            width=logo_width,
            height=logo_height,
            preserveAspectRatio=True,
            mask='auto'
        )

    pdf.setFillColor(colors.white)
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(35, height - 57, "FreshMart Vendor Order")

    pdf.setFillColor(colors.black)
    y = height - 105

    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(35, y, "Order Details")

    y -= 22
    pdf.setFont("Helvetica", 10)

    pdf.drawString(35, y, f"Order ID: {order.id}")
    pdf.drawString(320, y, f"Date: {order.created_at.strftime('%d-%m-%Y')}")

    y -= 18
    pdf.drawString(35, y, f"Customer: {order.customer_name}")

    y -= 18
    pdf.drawString(35, y, f"Username: {order.user.username}")

    y -= 18
    pdf.drawString(35, y, f"Phone: {order.phone}")

    y -= 18
    pdf.drawString(35, y, f"Payment: {order.payment_method}")

    y -= 18
    pdf.drawString(35, y, f"Status: {order.order_status}")

    y -= 18

    clean_address = (
        order.address.replace("\n", " ")
        .replace("\r", " ")
        .replace("■", "")
        .replace("█", "")
        .strip()
    )

    pdf.drawString(35, y, f"Address: {clean_address[:75]}")

    # TABLE
    y -= 35

    pdf.setFillColor(colors.HexColor("#EAEAEA"))
    pdf.rect(30, y, width - 60, 22, fill=1)

    pdf.setFillColor(colors.black)
    pdf.setFont("Helvetica-Bold", 10)

    pdf.drawString(38, y + 7, "Product")
    pdf.drawString(240, y + 7, "Qty")
    pdf.drawString(290, y + 7, "Weight")
    pdf.drawString(380, y + 7, "Price")
    pdf.drawString(475, y + 7, "Subtotal")

    y -= 22
    pdf.setFont("Helvetica", 10)

    for item in items:
        pdf.line(30, y, width - 30, y)

        pdf.drawString(38, y - 15, item.product.name[:28])
        pdf.drawString(242, y - 15, str(item.quantity))
        pdf.drawString(292, y - 15, item.weight)
        pdf.drawString(380, y - 15, f"Rs.{item.price}")
        pdf.drawString(475, y - 15, f"Rs.{item.subtotal}")

        y -= 24

    pdf.line(30, y, width - 30, y)

    y -= 38
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawRightString(width - 35, y, f"Total Amount: Rs.{order.total_price}")

    pdf.save()
    return response

@staff_member_required
def vendor_orders_export(request):

    month_value = request.GET.get('month')
    export_type = request.GET.get('type')

    if not month_value:
        return redirect('/vendor-orders/')

    year, month = month_value.split('-')

    orders = Order.objects.filter(
        created_at__year=year,
        created_at__month=month
    ).order_by('-id')

    total_orders = orders.count()

    delivered = orders.filter(
        order_status='Delivered'
    ).count()

    cancelled = orders.filter(
        order_status='Cancelled'
    ).count()

    revenue = orders.aggregate(
        total=Sum('total_price')
    )['total'] or 0

    month_title = f"{month_name[int(month)]} {year}"

    # ================= CSV =================
    if export_type == 'csv':

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename=orders_{month_value}.csv'

        writer = csv.writer(response)

        writer.writerow([
            'Order ID',
            'Customer',
            'Phone',
            'Status',
            'Payment',
            'Total',
            'Date'
        ])

        for order in orders:
            writer.writerow([
                order.id,
                order.customer_name,
                order.phone,
                order.order_status,
                order.payment_method,
                order.total_price,
                order.created_at.strftime('%d-%m-%Y')
            ])

        return response

    # ================= PDF =================
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=orders_{month_value}.pdf'

    doc = SimpleDocTemplate(
        response,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()
    elements = []

    # 🔥 ADD LOGO (TOP CENTER)
    logo_path = os.path.join(settings.BASE_DIR, 'static/images/logo.png')

    if os.path.exists(logo_path):
        logo = Image(logo_path, width=120, height=60)
        logo.hAlign = 'CENTER'
        elements.append(logo)
        elements.append(Spacer(1, 15))

    # HEADER
    title = Paragraph(
        f"<font size=20><b>FreshMart Monthly Report</b></font>",
        styles['Title']
    )

    subtitle = Paragraph(
        f"<font size=12>{month_title}</font>",
        styles['Normal']
    )

    elements.append(title)
    elements.append(Spacer(1, 8))
    elements.append(subtitle)
    elements.append(Spacer(1, 20))

    # SUMMARY TABLE
    summary_data = [
        ['Total Orders', total_orders],
        ['Delivered', delivered],
        ['Cancelled', cancelled],
        ['Revenue', f'Rs. {revenue}']
    ]

    summary = Table(summary_data, colWidths=[250, 220])

    summary.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 1, colors.grey),
        ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#D9F2E6')),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('ALIGN', (1,0), (1,-1), 'CENTER'),
    ]))

    elements.append(summary)
    elements.append(Spacer(1, 25))

    # ORDERS TABLE
    data = [[
        'ID',
        'Customer',
        'Status',
        'Payment',
        'Total',
        'Date'
    ]]

    for order in orders:
        data.append([
            str(order.id),
            order.customer_name[:18],
            order.order_status,
            order.payment_method,
            f'Rs.{order.total_price}',
            order.created_at.strftime('%d-%m')
        ])

    table = Table(data, colWidths=[45, 140, 90, 90, 80, 70])

    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.green),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ROWBACKGROUNDS',
            (0,1), (-1,-1),
            [colors.whitesmoke, colors.lightgrey]
        )
    ]))

    elements.append(table)
    elements.append(Spacer(1, 20))

    # FOOTER
    footer = Paragraph(
        "<i>Generated by FreshMart Vendor Panel</i>",
        styles['Normal']
    )

    elements.append(footer)

    doc.build(elements)

    return response