<<<<<<< HEAD
Flask Backend API for Kicktern Internship Task

Steps to run:
1. pip install -r requirements.txt
2. python app.py
3. Open http://127.0.0.1:5000

APIs:
- POST /api/contact
- POST /api/service-inquiry
- POST /api/admin/register
- POST /api/admin/login
- GET /api/admin/contacts
- GET /api/admin/inquiries
- PUT /api/admin/inquiry/<id>
- DELETE /api/admin/inquiry/<id>
=======
# Backend Development Internship Task – 1

## Project Description
This project is a backend REST API built as part of the Kicktern Backend Development Internship Task – 1.

The application allows users to:
- Register (Signup)
- Login using JWT Authentication
- Create tasks
- View tasks

## Features Implemented
- User authentication using email and password
- JWT-based authentication for protected routes
- CRUD operations for tasks
- Database integration using SQLite
- API testing using Postman

## Technologies Used
- Python
- Flask
- Flask-JWT-Extended
- Flask-SQLAlchemy
- SQLite
- Postman

## API Endpoints
- POST /signup – User registration
- POST /login – User login
- POST /tasks – Add task (Protected)
- GET /tasks – Fetch tasks (Protected)

## How to Run the Project
1. Install dependencies:
   pip install -r requirements.txt

2. Run the server:
   python app.py

3. Test APIs using Postman
>>>>>>> e98609fd6ed9eba558c0f190089624dfb279f8e9
