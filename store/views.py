# FILE: store/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Product
from accounts.models import CustomerProfile
from orders.models import Order, OrderItem

from django.core.exceptions import PermissionDenied

def customer_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_staff:
            raise PermissionDenied
        return view_func(request, *args, **kwargs)
    return wrapper

from django.core.paginator import Paginator

import razorpay
from django.conf import settings

# ✅ EMAIL IMPORTS
from django.core.mail import EmailMessage

# (Optional invoice import — safe)
try:
    from orders.views import generate_invoice_pdf
except:
    generate_invoice_pdf = None


# ================================
# ✅ EMAIL HELPER FUNCTION
# ================================
def send_order_email(order, request, delivered=False):

    if not request.user.email:
        return

    if delivered:
        subject = f"Order Delivered - FreshMart (#{order.id})"
        message = f"""
Hello {order.customer_name},

Your order #{order.id} has been successfully delivered 🎉

Total: ₹{order.total_price}

Thank you for shopping with FreshMart!
See you again soon ❤️
        """
    else:
        subject = f"Order Confirmed - FreshMart (#{order.id})"
        message = f"""
Hello {order.customer_name},

Your order #{order.id} has been placed successfully.

Total: ₹{order.total_price}

We are preparing your order 🚀
        """

    email = EmailMessage(
        subject,
        message,
        'your_email@gmail.com',
        [request.user.email],
    )

    # ✅ Attach invoice if available
    if generate_invoice_pdf:
        try:
            pdf = generate_invoice_pdf(order)
            email.attach(f"invoice_{order.id}.pdf", pdf, 'application/pdf')
        except:
            pass

    email.send(fail_silently=True)


def home(request):
    return render(request, 'landing.html')

@login_required
@customer_required
def customer_dashboard(request):
    return render(request, 'customer_dashboard.html')


@login_required
@customer_required
def fruits(request):

    query = request.GET.get('q', '')

    products = Product.objects.filter(category='Fruit', is_available=True)

    if query:
        products = products.filter(name__icontains=query)

    cart = request.session.get('cart', {})

    return render(request, 'fruits.html', {
        'products': products,
        'cart': cart,
        'query': query
    })


@login_required
@customer_required
def vegetables(request):

    query = request.GET.get('q', '')

    products = Product.objects.filter(category='Vegetable', is_available=True)

    if query:
        products = products.filter(name__icontains=query)

    cart = request.session.get('cart', {})

    return render(request, 'vegetables.html', {
        'products': products,
        'cart': cart,
        'query': query
    })


@login_required
@customer_required
def add_to_cart(request, product_id):

    cart = request.session.get('cart', {})

    product = get_object_or_404(
        Product,
        id=product_id,
        is_available=True
    )

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id]['qty'] += 1
    else:
        cart[product_id] = {
            'product_id': product.id,
            'qty': 1,
            'weight': '1kg'
        }

    request.session['cart'] = cart
    request.session.modified = True

    return redirect(
        request.META.get(
            'HTTP_REFERER',
            '/customer-dashboard/'
        )
    )


@login_required
@customer_required
def cart_view(request):

    cart = request.session.get('cart', {})
    cart_items = []
    grand_total = 0

    for key, item in cart.items():

        try:
            product = Product.objects.get(
                id=item['product_id']
            )
        except Product.DoesNotExist:
            continue

        qty = item['qty']
        weight = item['weight']

        base_price = float(product.price)

        if weight == '250g':
            price = base_price * 0.25
        elif weight == '500g':
            price = base_price * 0.50
        elif weight == '1.5kg':
            price = base_price * 1.5
        elif weight == '2kg':
            price = base_price * 2
        elif weight == '2.5kg':
            price = base_price * 2.5
        elif weight == '3kg':
            price = base_price * 3
        else:
            price = base_price

        total = price * qty
        grand_total += total

        cart_items.append({
            'product': product,
            'qty': qty,
            'weight': weight,
            'price': price,
            'total': total
        })

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'grand_total': grand_total
    })


@login_required
@customer_required
def increase_cart(request, product_id):

    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        cart[product_id]['qty'] += 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('/cart/')


@login_required
@customer_required
def decrease_cart(request, product_id):

    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:

        cart[product_id]['qty'] -= 1

        if cart[product_id]['qty'] <= 0:
            del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('/cart/')


@login_required
@customer_required
def remove_cart(request, product_id):

    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    next_url = request.GET.get('next')

    if next_url:
        return redirect(next_url)

    return redirect('/cart/')


@login_required
@customer_required
def update_cart_weight(request, product_id):

    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        cart[product_id]['weight'] = request.GET.get(
            'weight',
            '1kg'
        )

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('/cart/')


@login_required
@customer_required
def checkout(request):

    profile, created = CustomerProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        full_name = request.POST['full_name']
        phone = request.POST['phone']
        address = request.POST['address']
        payment = request.POST['payment']

        profile.full_name = full_name
        profile.phone = phone
        profile.address = address
        profile.save()

        cart = request.session.get('cart', {})

        if not cart:
            return redirect('/cart/')

        total = 0

        for key, item in cart.items():

            product = Product.objects.get(
                id=item['product_id']
            )

            qty = item['qty']
            weight = item['weight']

            price = float(product.price)

            if weight == '250g':
                price *= 0.25

            elif weight == '500g':
                price *= 0.50

            elif weight == '1.5kg':
                price *= 1.5

            elif weight == '2kg':
                price *= 2

            elif weight == '2.5kg':
                price *= 2.5

            elif weight == '3kg':
                price *= 3

            total += price * qty

        # =====================================
        # ✅ RAZORPAY PAYMENT FLOW
        # =====================================

        if payment == "Razorpay":

            client = razorpay.Client(auth=(
                settings.RAZORPAY_KEY_ID,
                settings.RAZORPAY_KEY_SECRET
            ))

            razorpay_order = client.order.create({

                "amount": int(total * 100),
                "currency": "INR",
                "payment_capture": "1"

            })

            request.session['checkout_data'] = {

                'customer_name': full_name,
                'phone': phone,
                'address': address,
                'total': total,
                'razorpay_order_id': razorpay_order['id']

            }

            request.session.modified = True

            return render(request, 'razorpay_payment.html', {

                'razorpay_order_id': razorpay_order['id'],
                'razorpay_key': settings.RAZORPAY_KEY_ID,
                'amount': int(total * 100),
                'customer_name': full_name,
                'email': request.user.email,
                'phone': phone,

            })

        # =====================================
        # ✅ COD FLOW
        # =====================================

        payment_status = 'Pending'

        order = Order.objects.create(

            user=request.user,
            customer_name=full_name,
            address=address,
            phone=phone,
            total_price=total,
            payment_method=payment,
            payment_status=payment_status,
            order_status='Pending'

        )

        for key, item in cart.items():

            product = Product.objects.get(
                id=item['product_id']
            )

            qty = item['qty']
            weight = item['weight']

            price = float(product.price)

            if weight == '250g':
                price *= 0.25

            elif weight == '500g':
                price *= 0.50

            elif weight == '1.5kg':
                price *= 1.5

            elif weight == '2kg':
                price *= 2

            elif weight == '2.5kg':
                price *= 2.5

            elif weight == '3kg':
                price *= 3

            subtotal = price * qty

            OrderItem.objects.create(

                order=order,
                product=product,
                quantity=qty,
                weight=weight,
                price=price,
                subtotal=subtotal

            )

        request.session.pop('cart', None)
        request.session.modified = True

        # ✅ EMAIL
        send_order_email(order, request)

        return redirect('/payment-success/')

    return render(request, 'checkout.html', {
        'profile': profile
    })


@login_required
@customer_required
def razorpay_payment(request):

    data = request.session.get('checkout_data')

    if not data:
        return redirect('/checkout/')

    return render(request, 'razorpay_payment.html', {
        'data': data
    })


@login_required
@customer_required
def razorpay_success(request):

    data = request.session.get('checkout_data')
    cart = request.session.get('cart', {})

    if not data or not cart:
        return redirect('/cart/')

    order = Order.objects.create(
        user=request.user,
        customer_name=data['customer_name'],
        address=data['address'],
        phone=data['phone'],
        total_price=data['total'],
        payment_method='Razorpay',
        payment_status='Paid',
        order_status='Pending'
    )

    for key, item in cart.items():

        product = Product.objects.get(id=item['product_id'])

        qty = item['qty']
        weight = item['weight']

        price = float(product.price)

        if weight == '250g': price *= 0.25
        elif weight == '500g': price *= 0.50
        elif weight == '1.5kg': price *= 1.5
        elif weight == '2kg': price *= 2
        elif weight == '2.5kg': price *= 2.5
        elif weight == '3kg': price *= 3

        subtotal = price * qty

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=qty,
            weight=weight,
            price=price,
            subtotal=subtotal
        )

    request.session.pop('cart', None)
    request.session.modified = True

    # ✅ EMAIL HERE ALSO
    send_order_email(order, request)

    return redirect('/payment-success/')


@login_required
@customer_required
def payment_success(request):
    return render(request, 'payment_success.html')


@login_required
@customer_required
def profile_page(request):

    profile, created = CustomerProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        changes = []

        # ===== USER FIELDS =====
        new_name = request.POST.get("name")
        new_email = request.POST.get("email")

        if new_name != request.user.first_name:
            request.user.first_name = new_name
            changes.append("name")

        if new_email != request.user.email:
            request.user.email = new_email
            changes.append("email")

        request.user.save()

        # ===== PROFILE FIELDS =====
        new_phone = request.POST.get("phone")
        new_address = request.POST.get("address")

        if new_phone != profile.phone:
            profile.phone = new_phone
            changes.append("phone")

        if new_address != profile.address:
            profile.address = new_address
            changes.append("address")

        profile.save()

        # ===== TOAST MESSAGES =====
        if len(changes) == 1:
            messages.success(request, f"{changes[0].capitalize()} updated successfully")
        elif len(changes) > 1:
            messages.success(request, "Changes updated successfully")
        else:
            messages.info(request, "No changes made")

        return redirect('/customer-dashboard/')

    return render(request, 'profile.html', {
        'profile': profile
    })

@login_required
@customer_required
def about(request):
    return render(request, 'about.html')


from django.db.models import Sum
from django.db.models.functions import ExtractMonth


@staff_member_required
def vendor_dashboard(request):
    return render(request, 'vendor_dashboard.html')


@staff_member_required
def vendor_revenue(request):

    total_revenue = Order.objects.filter(
        order_status='Delivered'
    ).aggregate(
        total=Sum('total_price')
    )['total'] or 0

    monthly_data = Order.objects.filter(
        order_status='Delivered'
    ).annotate(
        month=ExtractMonth('created_at')
    ).values('month').annotate(
        revenue=Sum('total_price')
    ).order_by('month')

    month_names = ['', 'Jan', 'Feb', 'Mar', 'Apr',
                   'May', 'Jun', 'Jul', 'Aug',
                   'Sep', 'Oct', 'Nov', 'Dec']

    labels = []
    values = []

    for item in monthly_data:
        labels.append(month_names[item['month']])
        values.append(float(item['revenue']))

    return render(request, 'vendor_revenue.html', {
        'total_revenue': total_revenue,
        'chart_labels': labels,
        'chart_values': values,
    })


@staff_member_required
def update_order_status(request, order_id, status):

    order = get_object_or_404(Order, id=order_id)

    order.order_status = status
    order.save()

    # ✅ EMAIL ON DELIVERY
    if status == 'Delivered':
        send_order_email(order, request, delivered=True)

    return redirect('/vendor-orders/')


@staff_member_required
def vendor_inventory(request):

    fruits = Product.objects.filter(category='Fruit')
    vegetables = Product.objects.filter(category='Vegetable')

    return render(request, 'vendor_inventory.html', {
        'fruits': fruits,
        'vegetables': vegetables,
        'total_products': Product.objects.count(),
        'available_products': Product.objects.filter(is_available=True).count(),
        'unavailable_products': Product.objects.filter(is_available=False).count(),
        'total_fruits': fruits.count(),
        'total_vegetables': vegetables.count(),
    })


@staff_member_required
def vendor_customers(request):

    customers = User.objects.filter(
        is_staff=False
    ).order_by('-id')

    return render(request, 'vendor_customers.html', {
        'customers': customers
    })


@staff_member_required
def add_product(request):

    if request.method == 'POST':

        Product.objects.create(
            name=request.POST['name'],
            price=request.POST['price'],
            category=request.POST['category'],
            image=request.FILES.get('image'),
            is_available=True
        )

        return redirect('/vendor-dashboard/')

    return render(request, 'add_product.html')


@staff_member_required
def edit_product(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':

        product.name = request.POST['name']
        product.price = request.POST['price']
        product.category = request.POST['category']

        if 'image' in request.FILES:
            product.image = request.FILES['image']

        product.is_available = (
            request.POST.get('is_available') == 'on'
        )

        product.save()

        return redirect('/vendor-inventory/')

    return render(request, 'edit_product.html', {
        'product': product
    })


@staff_member_required
def delete_product(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    product.delete()

    return redirect('/vendor-inventory/')


@staff_member_required
def toggle_product_status(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    product.is_available = not product.is_available
    product.save()

    return redirect('/vendor-inventory/')

from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request, 'welcome.html')