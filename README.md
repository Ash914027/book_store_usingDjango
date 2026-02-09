# Bookstore E-Commerce Platform

A Django-based e-commerce application for online bookstore management. This platform allows users to browse books, manage their shopping cart, and make purchases.

## Features

- **User Authentication**: User registration, login, and profile management
- **Book Catalog**: Browse and search for books with detailed information
- **Shopping Cart**: Add/remove items and manage quantities
- **Checkout**: Order placement with user information
- **Admin Panel**: Manage books, users, and orders

## Project Structure

```
bookstore/
├── accounts/          # User authentication and profiles
├── catalog/          # Book catalog and listing
├── cart/             # Shopping cart management
├── bookstore/        # Main project configuration
├── templates/        # Global templates
├── manage.py         # Django management script
└── db.sqlite3        # Database file
```

## Technology Stack

- **Backend**: Django
- **Database**: SQLite
- **Frontend**: HTML/CSS/JavaScript

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd bookstore
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install django
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`

## Usage

- **Admin Panel**: Navigate to `http://127.0.0.1:8000/admin/` to manage content
- **User Registration**: Create a new account at the registration page
- **Browse Books**: View available books in the catalog
- **Shopping Cart**: Add items and proceed to checkout

## Apps Overview

### Accounts
- User authentication
- User profiles with address and phone number
- Login records tracking

### Catalog
- Book listings
- Book details
- Category management

### Cart
- Shopping cart functionality
- Checkout process
- Order management

## Database Models

### User (accounts)
- Custom user model with address and phone fields
- Profile information
- Login history tracking

### Book (catalog)
- Book details (title, author, price, etc.)
- Inventory management

### Cart (cart)
- Cart items
- Order information

## Contributing

1. Fork the repository
2. Create your feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue in the repository.
