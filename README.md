# Chicago E-Commerce Project

A Django-based e-commerce web application consisting of two main apps:

- **Chicago**: Main landing page and user authentication (login, logout, registration, Google OAuth).
- **Store**: Product catalog and shopping features built with a Bootstrap template.

## Features

- User registration and login with email and Google OAuth using Django Allauth.
- Responsive design with Bootstrap templates.
- Separate apps for modular development.
- Secure user sessions and logout.
- Integration with social account providers.

## Getting Started

### Prerequisites

- Python 3.13+
- Django 5.2.3
- Virtual environment (recommended)
- SQLite3 (default DB, can be changed)

### Installation

1. Clone the repository:

   git clone https://github.com/yourusername/chicago-ecommerce.git
   cd chicago-ecommerce

2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. Install dependencies:

pip install -r requirements.txt

4. Apply migrations:

python manage.py migrate

5. Create a superuser (admin):

python manage.py createsuperuser


6. python manage.py createsuperuser

python manage.py runserver

7. Open your browser and go to http://127.0.0.1:8000/

Configuration
Configure site domain and site ID in Django admin under Sites.

Set up Google OAuth credentials and add them to settings.py.

Customize templates in the Chicago/templates and Store/templates folders.

Project Structure:

chicago_project/
├── Chicago/           # Main app (landing page, auth)
├── Store/             # Store app (product catalog, shopping)
├── chicago_project/   # Project settings and URLs
├── templates/         # Base templates and static assets
└── manage.py

Contributing
Feel free to fork this project and submit pull requests. Please ensure code quality and add tests for new features.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Created by Federico Almonacid



