# Django Ecommerce Website - HTMX/Tailwind

![Django](https://img.shields.io/badge/Django-4.x-green?style=for-the-badge&logo=django)
![HTMX](https://img.shields.io/badge/HTMX-1.x-blue?style=for-the-badge&logo=htmx)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.x-38B2AC?style=for-the-badge&logo=tailwindcss)

## Overview
This is a fully functional **Ecommerce Website** built with **Django**, using **HTMX** for dynamic interactions and **TailwindCSS** for styling. It supports user authentication, product management, cart system, checkout, and order tracking.

## Features
- 🔹 **User Authentication** (Signup, Login, Logout, Profile Management)
- 🛍 **Product Listings** (Categories, Search, Filtering)
- 🛒 **Shopping Cart** (Add, Remove, Update Items)
- 💳 **Checkout & Payment Integration**
- 📦 **Order Tracking & History**
- 🚀 **HTMX-powered Dynamic UI**
- 🎨 **TailwindCSS for Styling**

## Tech Stack
- **Backend:** Django 4.x, Django ORM, SQLite
- **Frontend:** HTMX, TailwindCSS
- **Authentication:** Django Allauth
- **Payment Gateway:** Stripe

## Installation
```sh
# Clone the repository
git clone https://github.com/yourusername/django-ecommerce-htmx.git
cd django-ecommerce-htmx

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

## Usage
- Open `http://127.0.0.1:8000/` in your browser.
- Register/Login to start shopping.
- Add products to the cart and proceed to checkout.
<!---
## Folder Structure
```
📂 django-ecommerce-htmx
├── 📁 ecommerce           # Main Django App
│   ├── 📁 templates       # HTML Templates (HTMX Components)
│   ├── 📁 static          # CSS, JS, Images
│   ├── 📄 views.py        # Django Views
│   ├── 📄 models.py       # Database Models
│   ├── 📄 urls.py         # URL Configurations
├── 📄 manage.py          # Django Management Script
├── 📄 requirements.txt    # Dependencies
└── 📄 README.md           # Project Documentation
```
--->
## Contributing
Feel free to contribute to this project by opening issues or submitting pull requests.

## License
This project is licensed under the MIT License.

---
Made with ❤️ using Django, HTMX, and TailwindCSS!
