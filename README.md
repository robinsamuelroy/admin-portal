# Admin Portal - AdminHub

## Overview
Admin Portal is a Django-based application designed to manage customer data and invoices. It features a modern user interface with authentication, customer management, and invoice management functionalities (CRUD Operations).

## Features
- **User Authentication:** Secure login/logout functionality.
- **Customer Management:** Add, edit, and list customers.
- **Invoice Management:** Create, edit, and list invoices.
- **Responsive Design:** Mobile-friendly interface.
- **Modern UI:** Clean and aesthetic design using Tailwind CSS.

## Technologies Used
- Django
- PostgreSQL
- Tailwind CSS
- HTML5
- CSS3

## Development Process

### Project Initialization
- Created a new Django project and application.
- Configured settings, including database setup with PostgreSQL.

### Authentication
- Implemented user authentication using Django's built-in authentication system.
- Created login and logout views and templates.

### Customer Management and Invoice Management
- Designed models for Customer and Invoice data.
- Created views and templates for listing, creating, and editing customers and invoices.

#### Customer Section
- **List Page:** Display a list of customers with basic information.
- **Create Page:** Allow the addition of a new customer with the following fields: ID, Name, Phone, Email, Address.
- **Edit Page:** Enable modification of existing customer details.

#### Invoice Section
- **List Page:** Display a list of invoices with basic information.
- **Create Page:** Allow the creation of a new invoice with the following fields: ID, Customer (selected from existing customers), Date, Amount, Status (Unpaid/Paid/Cancelled).
- **Edit Page:** Enable modification of existing invoice details.

### User Interface
- Utilized Tailwind CSS for styling and responsive design.
- Designed a clean and modern interface with a sidebar for navigation.

## Setup Instructions

### Prerequisites
- Python 3.8
- PostgreSQL
- Git

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/robinsamuelroy/admin-portal.git
    cd admin_portal
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure PostgreSQL database:**
    - Create a PostgreSQL database and user:
    ```sql
    CREATE DATABASE admin_portal;
    CREATE USER your_username WITH PASSWORD 'your_password';
    ALTER ROLE your_username SET client_encoding TO 'utf8';
    ALTER ROLE your_username SET default_transaction_isolation TO 'read committed';
    ALTER ROLE your_username SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE admin_portal TO your_username;
    ```

5. **Update `settings.py`:**
    - Edit the `DATABASES` section in `admin_portal/settings.py` with your database credentials:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'admin_portal',
            'USER': 'your_username',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    ```

6. **Apply migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

8. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

9. **Access the application:**
    - Open your web browser and go to `http://127.0.0.1:8000/`.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## Contact
For any inquiries, please contact robinroy.career@gmail.com.
