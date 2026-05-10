# <div>🌱 <span style="font-size:50px;">FreshMart – Online Grocery System</span></div>

FreshMart is a Django-based full-stack e-commerce web application for online fruit and vegetable ordering.
It includes separate customer and vendor modules with complete order lifecycle management, payment processing, inventory tracking, and invoice generation.
The project demonstrates production-style deployment using AWS EC2, Nginx, and Gunicorn.

---

## 💡 Project Motivation

This project was built to solve a real-world problem observed in my locality. In my apartment, local fruit and vegetable vendors share daily product photos via WhatsApp, and customers place orders manually by selecting items from those images. This process is unstructured, difficult to track, and does not provide proper order history or revenue visibility for vendors.

## 🚀 Solution Approach

To solve this, I developed a web-based system that allows vendors to list products digitally, manage availability (show/hide items), track orders, monitor revenue, and streamline the entire ordering process. Customers can browse products anytime, place orders easily, and track their order status in a structured way.

This project is inspired by real-world hyperlocal grocery ordering workflows and aims to digitize small vendor operations.

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

🌐 **Internet Client** → ⚡ **Nginx (Reverse Proxy)** → 🚀 **Gunicorn (WSGI Server)** → 🐍 **Django FreshMart Application** → 🔐 **Authentication • Cart • Orders • Payments** → 🗄️ **Database Operations (SQLite / PostgreSQL)** → ✅ **Response Sent Back To Client**

---

# ✨ Core Features

## 👤 Customer Module
- User registration and login system  
- Product browsing (fruits & vegetables)  
- Cart management with quantity control  
- Checkout with delivery details  
- Razorpay payment integration  
- Order tracking system  
- Invoice generation  
- Profile management  

## 🏪 Vendor Module
- Product management (add/edit/delete)  
- Inventory control system  
- Order management dashboard  
- Order status updates (Pending, Packed, Shipped, Delivered)  
- Revenue tracking  

## 💳 Payments
- Razorpay payment gateway integration  
- Secure payment verification  
- COD support  
- Order confirmation system  

## 📧 Notifications
- Order confirmation emails  
- Delivery status updates  
- Invoice email support  

---

# ☁️ AWS Cloud Deployment

FreshMart is deployed on an AWS EC2 Ubuntu instance using a production-grade Django deployment setup.

### Production Deployment Stack :

- AWS EC2 (Ubuntu)
- Gunicorn WSGI Server
- Nginx Reverse Proxy
- Static & Media File Handling
- Security Group Configuration
- Public IP Based Hosting

---

# 🔐 Security Features

- Django authentication system  
- CSRF protection  
- Role-based access (Customer / Vendor)  
- Secure payment handling  
- Sensitive credentials excluded via environment variables  

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

# 1) Welcome / Authentication

| Screenshot | Description |
|------------|-------------|
| ![Welcome Screen](Snapshots/welcome.png) | FreshMart landing page with introduction and navigation |
| ![Login Page](Snapshots/login.png) | Secure login system for customers and vendors |

---

# 2) Customer Section

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

# 3) Vendor Section

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

# 👨‍💻 Project Summary

FreshMart is a real-world inspired e-commerce platform designed to simulate an online grocery ordering system with customer and vendor workflows.
It demonstrates practical experience in building, securing, and deploying a full-stack Django application on AWS using production-grade tools and architecture.

---

# 📜 License

This project is developed for educational and portfolio purposes.
