# <div>🌱 <span style="font-size:50px;">FreshMart – Online Grocery System</span></div>

FreshMart is a Django-based full-stack e-commerce web application for online fruit and vegetable ordering. Inspired by real-world hyperlocal grocery workflows, the project was developed to digitize small vendor operations where orders are typically managed manually through messaging platforms like WhatsApp. 

The platform enables vendors to manage products, inventory, orders, and revenue through a structured system, while customers can browse products, place orders, make payments, and track deliveries through an interactive web interface. It is deployed in a production-like environment using AWS EC2 with Nginx and Gunicorn.

---

# 🚀 Tech Stack

[![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazonaws&logoColor=white)](https://aws.amazon.com/ec2/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-E95420?logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?logo=gunicorn&logoColor=white)](https://gunicorn.org/)
[![Nginx](https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white)](https://nginx.org/)
[![Razorpay](https://img.shields.io/badge/Razorpay-Payment-02042B?logo=razorpay&logoColor=white)](https://razorpay.com/)
[![SQLite](https://img.shields.io/badge/SQLite-07405E?logo=sqlite&logoColor=white)](https://www.sqlite.org/)

---

# 🏗 Architecture & Request Flow

```bash
🌐 Internet Client
        ↓
⚡ Nginx (Reverse Proxy)
        ↓
🚀 Gunicorn (WSGI Server)
        ↓
🐍 Django FreshMart Application
        ↓
🔐 Authentication • Cart • Orders • Payments
        ↓
🗄️ Database Operations (SQLite / PostgreSQL)
        ↓
✅ Response Sent Back To Client
```

---

# ✨ Core Features

## 1) 👤 Customer Module
- User registration and login system  
- Product browsing (fruits & vegetables)  
- Cart management with quantity control  
- Checkout with delivery details  
- Razorpay payment integration  
- Order tracking system  
- Invoice generation  
- Profile management  

## 2) 🏪 Vendor Module
- Product management (add/edit/delete)  
- Inventory control system  
- Order management dashboard  
- Order status updates (Pending, Packed, Shipped, Delivered)  
- Revenue tracking  

## 3) 💳 Payments
- Razorpay payment gateway integration  
- Secure payment verification  
- COD support  
- Order confirmation system  

## 4) 📧 Notifications
- Order confirmation emails  
- Delivery status updates  
- Invoice email support  

## 5) 🔐 Security Features

- Django authentication with role-based access (Customer / Vendor)  
- CSRF protection and secure payment handling  
- Sensitive credentials managed via environment variables  

---

# 📂 Project Structure

```text
FreshMart/
│
├── accounts/
├── orders/
├── store/
├── templates/
├── static/
├── media/
├── config/
├── manage.py
├── requirements.txt
└── README.md
```

---

# 📸 Application Screenshots

## 1) Welcome / Authentication

| Screenshot | Description |
|------------|-------------|
| ![Welcome Screen](Snapshots/welcome.png) | FreshMart landing page with introduction and navigation |
| ![Login Page](Snapshots/login.png) | Secure login system for customers and vendors |

---

## 2) Customer Section

| Screenshot | Description |
|------------|-------------|
| ![Customer Dashboard](Snapshots/customer-dashboard.png) | Customer dashboard with navigation cards and shopping options |
| ![Customer Fruits](Snapshots/customer-fruits.png) | Fruits category product listing page |
| ![Customer Vegetables](Snapshots/customer-veg.png) | Vegetables category product listing page |
| ![Shopping Cart](Snapshots/cart.png) | Dynamic cart system with quantity and weight management |
| ![Checkout Page](Snapshots/checkout.png) | Checkout page with delivery and payment details |
| ![Order Success](Snapshots/order-success.png) | Successful order confirmation page |
| ![Invoice](Snapshots/invoice.png) | Generated PDF invoice for customer orders |

---

## 3) Vendor Section

| Screenshot | Description |
|------------|-------------|
| ![Vendor Dashboard](Snapshots/vendor-dashboard.png) | Vendor/admin dashboard overview |
| ![Vendor Products](Snapshots/vendor-products.png) | Inventory and product management system |
| ![Vendor Orders](Snapshots/vendor-orders.png) | Order processing and management panel |
| ![Vendor Revenue](Snapshots/revenue.png) | Revenue analytics and earnings overview |

---

# ⚡ Installation & Setup

```bash
git clone https://github.com/yourusername/freshmart.git && cd freshmart

python -m venv venv
# Activate:
For Windows: venv\Scripts\activate
For Linux/Mac: source venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

# 🔑 Environment Variables

Before running the project, configure the following credentials inside `settings.py` or environment variables:

```python
# Django Secret Key
SECRET_KEY = "YOUR_SECRET_KEY"

# Razorpay Credentials
RAZORPAY_KEY_ID = "YOUR_RAZORPAY_KEY"
RAZORPAY_KEY_SECRET = "YOUR_RAZORPAY_SECRET"

# Email Configuration
EMAIL_HOST_USER = "YOUR_EMAIL@gmail.com"
EMAIL_HOST_PASSWORD = "YOUR_APP_PASSWORD"
DEFAULT_FROM_EMAIL = "FreshMart <YOUR_EMAIL@gmail.com>"
```

---

# 🧠 Skills Demonstrated

- Django backend development  
- Full-stack web application design  
- Payment gateway integration (Razorpay)  
- Database design & management  
- AWS EC2 deployment  
- Nginx & Gunicorn configuration  
- Authentication & authorization systems  
- Order & inventory management systems  
- Production deployment workflow  

---
