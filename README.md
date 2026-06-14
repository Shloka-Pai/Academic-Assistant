# Academic Assistant Project

This project is built using Django and serves as an Academic Assistant platform designed to help students manage and access academic information efficiently.

## Available Commands

In the project directory, you can run:

### `python manage.py runserver`

Runs the application in development mode.

Open http://127.0.0.1:8000/ to view it in your browser.

The server will automatically reload when you make changes.

---

### `python manage.py makemigrations`

Creates new migration files based on changes made to Django models.

Run this command whenever you modify model definitions.

---

### `python manage.py migrate`

Applies database migrations and updates the database schema.

Make sure to run this command before starting the application.

---

### `python manage.py createsuperuser`

Creates an administrator account for accessing the Django Admin Panel.

After creating the account, visit:

http://127.0.0.1:8000/admin/

to manage application data.

---

### `python manage.py test`

Runs the project's test suite.

Use this command to verify that all components of the application are functioning correctly.

---

### `python manage.py collectstatic`

Collects all static files into a single directory for production deployment.

Required when deploying the application to a production server.

## Project Setup

### Clone the Repository

```bash
git clone <repository-url>
cd academic-assistant
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run the Development Server

```bash
python manage.py runserver
```

## Features

- **Constraint-Based Credit Management**
- **Real-Time Appointment System**
- **Faculty Cabin Locator**
- **Secure Authentication System**
- **User-Friendly Interface**
- **Responsive Design**
- **Efficient Scheduling**

## Technology Stack

- Python
- Django
- HTML
- CSS
- JavaScript
- Bootstrap
- SQLite

## Deployment

Before deployment, run:

```bash
python manage.py collectstatic
```

Update your Django settings:

```python
DEBUG = False
ALLOWED_HOSTS = ["your-domain.com"]
```

Configure your production database and web server according to your hosting provider.

## Learn More

To learn more about Django, visit:

https://docs.djangoproject.com/

To learn more about Python:

https://docs.python.org/

## Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.
