
# Ecommerce Management System (Django)

A robust ecommerce platform built with **Python** and **Django**. This system manages products, customer orders, and provides a powerful admin interface for inventory control.

## 🚀 Tech Stack

* **Framework:** Django (Python)
* **Database:** SQLite (Development) / PostgreSQL (Production)
* **Templating:** Django Template Language (HTML/CSS)
* **Styling:** Bootstrap 5

## 📦 Project Structure (Planned)
* **Core:** Project configuration and settings.
* **Products:** Catalog, categories, and inventory management.
* **Cart:** Session-based shopping cart for customers.
* **Orders:** Checkout process and order history.
* **Users:** Custom user model for customers and staff.

## 🛠️ How to Run Locally
1. Clone the repo:
   `git clone <your-repo-url>`
3. Create a virtual environment:
   `python -m venv venv`
4. Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
5. Install Django:
   `pip install django pillow`
6. Run migrations:
   `python manage.py migrate`
7. Start the server:
   `python manage.py runserver`
