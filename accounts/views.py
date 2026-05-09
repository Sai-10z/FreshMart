from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .models import CustomerProfile


# =========================
# ✅ SIGNUP
# =========================
def signup(request):

    # ❌ Prevent logged-in users from accessing signup
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('/vendor-dashboard/')
        else:
            return redirect('/customer-dashboard/')

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            user.first_name = request.POST.get("full_name", "")
            user.email = request.POST.get("email", "")
            user.save()

            CustomerProfile.objects.get_or_create(user=user)

            messages.success(request, "Customer account created successfully.")

            return redirect('/login/')

    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


# =========================
# ✅ LOGIN
# =========================
def custom_login(request):

    # ✅ BLOCK LOGIN PAGE IF ALREADY LOGGED IN
    if request.user.is_authenticated:

        if request.user.is_staff:
            return redirect('/vendor-dashboard/')
        else:
            return redirect('/customer-dashboard/')

    error = ""

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            messages.success(request, "Logged in successfully")

            # ✅ ROLE-BASED REDIRECT
            if user.is_staff:
                return redirect('/vendor-dashboard/')
            else:
                return redirect('/customer-dashboard/')

        else:
            error = "Invalid username or password"
            messages.error(request, error)

    return render(request, "login.html", {"error": error})


# =========================
# ✅ PROFILE (CUSTOMER ONLY)
# =========================
@login_required
def profile(request):

    # ❌ BLOCK VENDOR ACCESS
    if request.user.is_staff:
        return redirect('/vendor-dashboard/')

    profile, created = CustomerProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

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

        # ===== TOAST MESSAGE =====
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


# =========================
# ✅ LOGOUT
# =========================
def custom_logout(request):
    logout(request)
    request.session.flush()

    messages.error(request, "Logged out successfully")

    return redirect('welcome')


# =========================
# ✅ CHANGE PASSWORD
# =========================
@login_required
def change_password(request):

    # ❌ BLOCK VENDOR (optional but recommended)
    if request.user.is_staff:
        return redirect('/vendor-dashboard/')

    if request.method == 'POST':

        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()

            # 🔐 KEEP USER LOGGED IN
            update_session_auth_hash(request, user)

            messages.success(request, "Password updated successfully")

            return redirect('/profile/')

        else:
            messages.error(request, "Please fix the errors below")

    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {
        'form': form
    })