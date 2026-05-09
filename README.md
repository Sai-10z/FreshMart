# 🛒 Fresh Mart

A full-stack Django-based e-commerce web application for selling fresh fruits and vegetables online.  
Fresh Mart provides a seamless shopping experience for users along with a complete vendor management system, including cart handling, secure payments, and order processing.

This project demonstrates end-to-end web application development along with cloud deployment on AWS EC2 using Nginx and Gunicorn.

## 🚀 Tech Stack

[![AWS](https://img.shields.io/badge/AWS-EC2-FF9900?logo=amazonaws&logoColor=white)](https://aws.amazon.com/ec2/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-E95420?logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?logo=gunicorn&logoColor=white)](https://gunicorn.org/)
[![Nginx](https://img.shields.io/badge/Nginx-009639?logo=nginx&logoColor=white)](https://nginx.org/)
[![Razorpay](https://img.shields.io/badge/Razorpay-Payment-02042B?logo=razorpay&logoColor=white)](https://razorpay.com/)

- **Backend:** Django, Python  
- **Frontend:** HTML, CSS, Bootstrap  
- **Database:** SQLite / PostgreSQL  
- **Payment Gateway:** Razorpay  
- **Cloud Deployment:** AWS EC2  
- **Web Server:** Nginx + Gunicorn

## 🏗 Architecture

```text
Internet Client
      │
      ▼
   Nginx
(Reverse Proxy)
      │
      ▼
  Gunicorn
 (WSGI Server)
      │
      ▼
Django Fresh Mart Application
      │
      ▼
Database (SQLite / PostgreSQL)
```

Flow Explanation:

Client sends request from browser
Nginx handles incoming traffic and static files
Gunicorn processes Django application requests
Django handles business logic (cart, orders, payments)
Database stores user, product, and order data

## ⚙️ Features & Deployment Highlights

### 👤 User Features
- Secure user authentication (login & registration)
- Browse fresh fruits and vegetables by category
- Add products to cart and manage quantities
- Place orders with a smooth checkout flow
- View order history and track status

### 🏪 Vendor / Admin Features
- Add, update, and delete products
- Manage stock and inventory
- View and process customer orders

### 💳 Payment Integration
- Integrated Razorpay payment gateway
- Secure transaction handling
- Order confirmation after successful payment

### ☁️ Deployment Highlights
- Deployed on AWS EC2 Ubuntu instance
- Configured Gunicorn as WSGI server
- Nginx used as reverse proxy for production
- Static files served efficiently in production setup

# 📸 FreshMart - Application Screenshots

---

## 1. Index / Welcome + Login Page

| Screenshot | Description |
|------------|-------------|
| ![Welcome Screen](Snapshots/welcome.png) | Landing page displaying FreshMart branding and introductory tagline |
| ![Login Page](Snapshots/login.png) | Secure login interface where users/vendors authenticate using email/phone and password |

---

## 2. Customer Section

| Screenshot | Description |
|------------|-------------|
| ![Customer Dashboard](Snapshots/customer-dashboard.png) | Customer dashboard showing product categories, banners, and promotions |
| ![Customer Fruits](Snapshots/customer-fruits.png) | Fruits section displaying product grid with pricing and Add to Cart option |
| ![Customer Vegetables](Snapshots/customer-veg.png) | Vegetables section with searchable product listings and cart actions |
| ![Customer Cart](Snapshots/cart.png) | Shopping cart view with selected items, quantity controls, and price updates |
| ![Checkout Page](Snapshots/checkout.png) | Checkout page with address selection, order summary, and payment options |
| ![Order Success](Snapshots/order-success.png) | Order confirmation page showing successful purchase and order ID |
| ![Invoice](Snapshots/invoice.png) | Detailed invoice with purchased items, quantities, and total billing amount |

---

## 3. Vendor Section

| Screenshot | Description |
|------------|-------------|
| ![Vendor Dashboard](Snapshots/vendor-dashboard.png) | Vendor dashboard showing sales overview and key business metrics |
| ![Vendor Products](Snapshots/vendor-products.png) | Product management panel for adding, editing, and deleting items |
| ![Vendor Orders](Snapshots/vendor-orders.png) | Order management panel for tracking and updating order status |
| ![Revenue Overview](Snapshots/revenue.png) | Revenue analytics dashboard displaying monthly earnings trends |

---

## 📁 Note
All screenshots are stored in the `/Snapshots` directory of this repository.

> 📁 All screenshots are stored in the `/screenshots` directory of this repository.

## 👨‍💻 Project Summary

Fresh Mart is a full-stack e-commerce platform built to simulate a real-world online grocery store.  
It demonstrates strong backend development using Django along with practical implementation of payment gateways and cloud deployment.

This project highlights:
- End-to-end web application development
- Real-time order and inventory management system
- Secure payment integration using Razorpay
- Production deployment on AWS using EC2, Nginx, and Gunicorn

Overall, Fresh Mart reflects practical skills in building, deploying, and managing a scalable web application in a cloud environment.
