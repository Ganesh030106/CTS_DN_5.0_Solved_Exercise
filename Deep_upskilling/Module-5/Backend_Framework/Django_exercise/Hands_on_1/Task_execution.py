"""
HANDS-ON 1 Web Framework Foundations & Django Project Setup
"""
# TASK 1: Understand the Request-Response Cycle

"""
GET /api/courses/

Browser
   ↓
URL Router
   ↓
View
   ↓
Model
   ↓
Database
   ↓
View
   ↓
HTTP Response
   ↓
Browser

Middleware sits between the request and response cycle.
"""

# Built-in Middleware Examples

"""
1. SecurityMiddleware
   - Adds security headers
   - HTTPS related protection

2. SessionMiddleware
   - Handles user sessions
   - Stores session information
"""

# WSGI vs ASGI

"""
WSGI
-----
Synchronous request handling.
Used by traditional Django applications.

ASGI
-----
Asynchronous request handling.
Supports WebSockets and real-time applications.

Django uses WSGI by default.

Use ASGI when:
- Chat applications
- WebSockets
- Live notifications
- Async APIs
"""

# MVC vs MVT

"""
MVC
----
Model
View
Controller

Django MVT
-----------
Model
View
Template

Mapping:

MVC Model      -> Django Model
MVC View       -> Django Template
MVC Controller -> Django View
"""

# TASK 2: Django Project Setup Commands

"""
For Creating a Python Environment and Installing Django

Create Virtual Environment

   python -m venv venv

Activate

   venv\\Scripts\\activate

Install Django

   pip install django
"""

# TASK 3: Create Django Project

"""
The command to create a Django project named "coursemanager" is:
django-admin startproject coursemanager


To run the Django development server, navigate to the project directory and execute:
cd coursemanager


To start the server, use the command:
python manage.py runserver
"""

# TASK 4: Generated Files Explanation

# Adding the comments for the generated files in the Django project:

"""
settings.py
------------
Project configuration file.

urls.py
---------
Main URL routing configuration.

wsgi.py
---------
WSGI deployment entry point.

asgi.py
---------
ASGI deployment entry point.
"""

# TASK 5: Create Django App
"""
The command to create a Django app named "courses" is:

python manage.py startapp courses

"""

"""
Difference of the Project and App:

Project: Complete Django application.

App: Reusable module inside project.

One project can contain many apps.
"""

# TASK 6: Register App

"""
To register the "courses" app in the Django project, add it to the INSTALLED_APPS list in 
settings.py file

INSTALLED_APPS = [
    ...
    'courses',
]
"""

# TASK 7: Create View

"""To create a view in the "courses" app"""

"""
courses/views.py

from django.http import HttpResponse

def hello_view(request):
    return HttpResponse(
        "Course Management API is running"
    )
"""

# TASK 8: Create App URLs

"""
courses/urls.py

from django.urls import path
from .views import hello_view

urlpatterns = [
    path('hello/', hello_view),
]
"""

# TASK 9: Main URL Configuration

"""
coursemanager/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courses.urls')),
]
"""

# TASK 10: Verification

# To verify the Setup, Running the Django Setup

"""
Run:

python manage.py migrate

python manage.py runserver

Open the URL in the browser:

http://127.0.0.1:8000/api/hello/

Output:

Course Management API is running
"""
