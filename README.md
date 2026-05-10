# 🛒 FreshMart – Full Stack Django E-Commerce Web Application

FreshMart is a full-stack Django-based e-commerce web application designed for online fruit and vegetable ordering.  
The platform provides a complete customer shopping experience along with a powerful vendor/admin management system for handling products, orders, inventory, payments, invoices, and revenue tracking.

The project demonstrates real-world backend development, payment gateway integration, cloud deployment, and production server configuration using AWS EC2, Gunicorn, and Nginx.

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
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)](https://github.com/)

---

# 🏗 Architecture & Request Flow

<table width="100%">
<tr>

<td width="50%" valign="top">

### 🏗 System Architecture

```text
Internet Client
      ↓
Nginx
(Reverse Proxy)
      ↓
Gunicorn
(WSGI Server)
      ↓
Django FreshMart Application
      ↓
Database (SQLite / PostgreSQL)
```

</td>

<td width="50%" valign="top">

### ⚙️ Request Flow

```text
Client Request
      ↓
Nginx Receives Traffic
      ↓
Gunicorn Processes Django Requests
      ↓
Django Handles Business Logic
(Authentication / Cart / Orders / Payments)
      ↓
Database Operations
      ↓
Response Sent Back To Client
```

</td>

</tr>
</table>

---

# ✨ Core Features

## 👤 Customer Features

- User registration and authentication
- Customer dashboard with category navigation
- Browse fruits and vegetables separately
- Search products dynamically
- Add to cart / remove from cart
- Quantity and weight management
- Real-time cart total calculation
- Checkout and delivery details form
- Razorpay payment gateway integration
- Order placement and confirmation
- Order tracking with live status progress bar
- Invoice generation and download
- Profile management system
- Responsive mobile-friendly UI

---

## 🏪 Vendor / Admin Features

- Vendor dashboard with statistics overview
- Product inventory management
- Add / edit / delete products
- Enable or disable product availability
- Customer management panel
- Active order tracking
- Order status management:
  - Pending
  - Packed
  - Shipped
  - Delivered
  - Cancelled
- Revenue analytics dashboard
- Monthly revenue visualization
- Export order reports (CSV / PDF)
- Invoice generation for vendors

---

## 💳 Payment Integration

- Integrated Razorpay payment gateway
- Secure online transaction flow
- Razorpay order creation using backend API
- Payment verification flow
- COD support
- Payment success confirmation page

---

## 📧 Email Features

- Automatic order confirmation emails
- Delivery completion email notifications
- Invoice attachment support
- Customer communication automation

---

# ☁️ AWS Cloud Deployment

FreshMart is deployed on an AWS EC2 Ubuntu instance using a production-grade Django deployment setup.

## Production Deployment Stack

- AWS EC2 (Ubuntu)
- Gunicorn WSGI Server
- Nginx Reverse Proxy
- Static & Media File Handling
- Security Group Configuration
- Public IP Based Hosting

---

# 🔐 Security Features

- Django authentication system
- Protected customer/vendor routes
- Role-based access handling
- CSRF protection
- Secure payment handling
- Sensitive credentials excluded using `.gitignore`

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

# 1️⃣ Welcome / Authentication

| Screenshot | Description |
|------------|-------------|
| ![Welcome Screen](Snapshots/welcome.png) | FreshMart landing page with introduction and navigation |
| ![Login Page](Snapshots/login.png) | Secure login system for customers and vendors |

---

# 2️⃣ Customer Section

| Screenshot | Description |
|------------|-------------|
| ![Customer Dashboard](Snapshots/customer-dashboard.png) | Customer dashboard with navigation cards and shopping options |
| ![Customer Fruits](Snapshots/customer-fruits.png) | Fruits category product listing page |
| ![Customer Vegetables](Snapshots/customer-veg.png) | Vegetables category product listing page |
| ![Shopping Cart](Snapshots/cart.png) | Dynamic cart system with quantity and weight management |
| ![Checkout Page](Snapshots/checkout.png) | Checkout page with delivery and payment details |
| ![Razorpay Payment](Snapshots/razorpay.png) | Razorpay secure online payment gateway |
| ![Order Success](Snapshots/order-success.png) | Successful order confirmation page |
| ![Customer Orders](Snapshots/customer-orders.png) | Customer order tracking with live status progress |
| ![Invoice](Snapshots/invoice.png) | Generated PDF invoice for customer orders |

---

# 3️⃣ Vendor Section

| Screenshot | Description |
|------------|-------------|
| ![Vendor Dashboard](Snapshots/vendor-dashboard.png) | Vendor/admin dashboard overview |
| ![Vendor Products](Snapshots/vendor-products.png) | Inventory and product management system |
| ![Vendor Orders](Snapshots/vendor-orders.png) | Order processing and management panel |
| ![Vendor Revenue](Snapshots/revenue.png) | Revenue analytics and earnings overview |
| ![Vendor Customers](Snapshots/vendor-customers.png) | Customer management interface |

---

# 📁 Screenshots Directory

> All screenshots used in this README are stored inside the `/Snapshots` directory.

---

# ⚡ Installation & Setup

## Clone Repository

```bash
git clone https://github.com/yourusername/freshmart.git
cd freshmart
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Run Migrations

```bash
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Start Development Server

```bash
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

# 📦 Git Ignore

Sensitive files excluded from GitHub:

```text
.env
db.sqlite3
media/
venv/
__pycache__/
```

---

# 🧠 Skills Demonstrated

- Full Stack Web Development
- Django Backend Development
- Payment Gateway Integration
- REST-style Request Handling
- Authentication & Authorization
- Cloud Deployment
- Linux Server Management
- Nginx Configuration
- Gunicorn Setup
- Database Operations
- Inventory Management
- Order Processing Systems
- Responsive UI Design
- AWS EC2 Deployment
- Production Deployment Workflow

---

# 👨‍💻 Project Summary

FreshMart is a real-world inspired e-commerce platform developed to simulate an online grocery delivery system with both customer and vendor workflows.

The project demonstrates practical experience in:

- Building scalable Django web applications
- Implementing secure payment gateways
- Managing orders and inventory systems
- Deploying production applications on AWS
- Configuring Nginx and Gunicorn servers
- Handling full-stack development workflows

This project reflects strong hands-on skills in backend engineering, cloud deployment, and complete web application lifecycle management.

---

# 📜 License

This project is developed for educational and portfolio purposes.
