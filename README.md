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

## 📸 Output / Screenshots

<p align="center">
  <img src="home-page.png" alt="Home Page" width="80%">
</p>

<p align="center">
  <img src="product-page.png" alt="Product Page" width="80%">
</p>

<p align="center">
  <img src="cart-page.png" alt="Cart Page" width="80%">
</p>

<p align="center">
  <img src="checkout-page.png" alt="Checkout Page" width="80%">
</p>

**Note:**  
These screenshots represent the core user flow of Fresh Mart — from browsing products to completing a purchase via Razorpay checkout.

## 👨‍💻 Project Summary

Fresh Mart is a full-stack e-commerce platform built to simulate a real-world online grocery store.  
It demonstrates strong backend development using Django along with practical implementation of payment gateways and cloud deployment.

This project highlights:
- End-to-end web application development
- Real-time order and inventory management system
- Secure payment integration using Razorpay
- Production deployment on AWS using EC2, Nginx, and Gunicorn

Overall, Fresh Mart reflects practical skills in building, deploying, and managing a scalable web application in a cloud environment.

